#!/usr/bin/env python3
"""
Volt PRDs MCP Server — Knowledge agent for the Volt Money product repository.
Serves search, topic summaries, full PRD content, and related PRD discovery.
"""

import asyncio
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

ROOT = Path(__file__).resolve().parent
PRODUCT_REPO = ROOT / "Product Repository"
KNOWLEDGE = ROOT / "knowledge"
DB_PATH = KNOWLEDGE / "index.db"
SUMMARIES_PATH = KNOWLEDGE / "summaries"
GRAPHIFY_PATH = ROOT / "graphify-out"
GRAPH_JSON = GRAPHIFY_PATH / "graph.json"
GRAPH_REPORT = GRAPHIFY_PATH / "GRAPH_REPORT.md"

sys.path.insert(0, str(ROOT))


# ---------------------------------------------------------------------------
# Auto-build index if missing
# ---------------------------------------------------------------------------

def ensure_index():
    if not DB_PATH.exists():
        print("[volt-prds] Index not found — building now (first run)...", file=sys.stderr)
        from _build import build_index, build_summaries
        build_index(verbose=False)
        build_summaries(verbose=False)
        print("[volt-prds] Index ready.", file=sys.stderr)


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------

def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def fts_search(query: str, limit: int = 5) -> list[dict]:
    conn = get_db()
    try:
        rows = conn.execute(
            """
            SELECT f.title, f.file_path, f.topic_areas, f.status, f.last_edited,
                   snippet(files_fts, 1, '**', '**', '...', 32) AS snippet,
                   bm25(files_fts) AS rank
            FROM files_fts
            JOIN files f ON f.id = files_fts.rowid
            WHERE files_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (query, limit)
        ).fetchall()
        return [dict(r) for r in rows]
    except Exception:
        rows = conn.execute(
            """
            SELECT title, file_path, topic_areas, status, last_edited,
                   substr(content, 1, 300) AS snippet
            FROM files
            WHERE title LIKE ? OR content LIKE ?
            LIMIT ?
            """,
            (f"%{query}%", f"%{query}%", limit)
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_file_by_name(name: str) -> dict | None:
    conn = get_db()
    name_l = name.lower().strip()
    row = conn.execute(
        "SELECT * FROM files WHERE lower(title) = ?", (name_l,)
    ).fetchone()
    if not row:
        rows = conn.execute(
            "SELECT * FROM files WHERE lower(title) LIKE ? ORDER BY length(title)",
            (f"%{name_l}%",)
        ).fetchall()
        row = rows[0] if rows else None
    conn.close()
    return dict(row) if row else None


def get_mentions_from_index(title: str, limit: int = 8) -> list[dict]:
    """Files that explicitly mention this PRD's title in their content."""
    conn = get_db()
    title_l = title.lower()
    rows = conn.execute(
        """
        SELECT title, file_path, topic_areas, status, last_edited
        FROM files
        WHERE lower(content) LIKE ? AND lower(title) != ?
        ORDER BY last_edited DESC
        LIMIT ?
        """,
        (f"%{title_l}%", title_l, limit)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Graph Index — maps graphify labels to SQLite titles
# ---------------------------------------------------------------------------

class GraphIndex:
    """Pre-built mapping from graphify node labels to SQLite file IDs."""

    def __init__(self):
        self._label_to_db_id: dict[str, int] = {}     # graphify label -> SQLite file id
        self._label_to_filepath: dict[str, str] = {}  # graphify label -> relative file path
        self._node_id_to_label: dict[str, str] = {}   # graphify node id -> label
        self._links: list[dict] = []
        self._loaded = False

    def load(self):
        if not GRAPH_JSON.exists() or not DB_PATH.exists():
            return
        try:
            data = json.loads(GRAPH_JSON.read_text())
            self._node_id_to_label = {n["id"]: n["label"] for n in data["nodes"]}
            self._links = data["links"]

            conn = sqlite3.connect(DB_PATH)
            rows = conn.execute("SELECT id, title, file_path FROM files").fetchall()
            conn.close()

            title_to_id       = {r[1].lower().strip(): r[0] for r in rows}
            title_to_filepath = {r[1].lower().strip(): r[2] for r in rows}

            matched = 0
            for label in self._node_id_to_label.values():
                label_l = label.lower().strip()
                if label_l in title_to_id:
                    self._label_to_db_id[label]    = title_to_id[label_l]
                    self._label_to_filepath[label] = title_to_filepath[label_l]
                    matched += 1

            self._loaded = True
            print(f"[volt-prds] GraphIndex loaded: {matched}/{len(self._node_id_to_label)} labels matched", file=sys.stderr)
        except Exception as e:
            print(f"[volt-prds] GraphIndex load failed: {e}", file=sys.stderr)

    def _find_label(self, title: str) -> str | None:
        """Find the best-matching graphify label for a given title."""
        title_l = title.lower().strip()
        # Exact
        for label in self._label_to_db_id:
            if label.lower().strip() == title_l:
                return label
        # Substring (shortest label wins to avoid overly broad matches)
        candidates = [l for l in self._label_to_db_id if title_l in l.lower() or l.lower() in title_l]
        if candidates:
            return min(candidates, key=len)
        return None

    def _label_to_node_id(self, label: str) -> str | None:
        for nid, lbl in self._node_id_to_label.items():
            if lbl == label:
                return nid
        return None

    def get_related(self, title: str, limit: int = 12) -> list[dict]:
        if not self._loaded:
            return []

        label = self._find_label(title)
        if not label:
            return []

        node_id = self._label_to_node_id(label)
        if not node_id:
            return []

        seen = set()
        related = []
        for link in self._links:
            other_id = None
            relation = link["relation"]

            if link["source"] == node_id:
                other_id = link["target"]
            elif link["target"] == node_id:
                other_id = link["source"]

            if other_id and other_id not in seen:
                seen.add(other_id)
                other_label = self._node_id_to_label.get(other_id, "")
                if other_label and other_label != label:
                    related.append({
                        "label": other_label,
                        "relation": relation,
                        "confidence": link.get("confidence_score", 0.0),
                        "in_index": other_label in self._label_to_db_id,
                    })

        # Sort: indexed PRDs first, then by confidence descending
        related.sort(key=lambda r: (not r["in_index"], -r["confidence"]))
        return related[:limit]

    def get_filepath(self, label: str) -> str:
        return self._label_to_filepath.get(label, "")

    @property
    def loaded(self) -> bool:
        return self._loaded


# Singleton loaded at server startup
_graph = GraphIndex()


# ---------------------------------------------------------------------------
# Format helpers
# ---------------------------------------------------------------------------

def format_search_results(results: list[dict], query: str) -> str:
    if not results:
        return f"No results found for **\"{query}\"**."

    lines = [f"## Search results for \"{query}\"\n"]
    for i, r in enumerate(results, 1):
        topics = r.get("topic_areas", "").replace(",", " · ")
        abs_path = str(ROOT / r["file_path"]) if r.get("file_path") else ""
        lines.append(
            f"### {i}. {r['title']}\n"
            f"`{abs_path}`\n"
            f"**Topics:** {topics}  |  **Status:** {r.get('status') or '—'}  |  **Last edited:** {r.get('last_edited') or '—'}\n\n"
            f"{r.get('snippet', '').strip()}\n"
        )
    lines.append(f"\n*Use `get_prd` with a title above for the full document.*")
    return "\n".join(lines)


def format_prd(row: dict) -> str:
    file_path = ROOT / row["file_path"]
    abs_path = str(file_path)
    if file_path.exists():
        content = file_path.read_text(errors="ignore")
        content = re.sub(r'!\[.*?\]\(data:image/[^)]+\)', '[image removed]', content)
        return f"`{abs_path}`\n\n{content}"
    return row.get("content", "Content not available.")


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

server = Server("volt-prds")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search",
            description=(
                "Search the entire Volt product knowledge base — PRDs, process notes, journeys, FAQs. "
                "Returns the most relevant results with context snippets. "
                "Use this for any question about how a feature works, what a flow does, or finding a specific PRD."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "What you're looking for"},
                    "limit": {"type": "integer", "default": 5, "description": "Max results (default 5)"},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="get_topic",
            description=(
                "Get the current state summary for a product topic area — synthesised from all related PRDs, "
                "newest first. Use this for 'how does X work today' questions. "
                "Topics: pledge, mandate, kyc, repayment, disbursement, foreclosure, "
                "loan-origination, loan-management, comms, ops-tools, b2b, mfd, analytics, compliance, credit-limit, collections."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Topic name (e.g. 'pledge', 'kyc', 'mandate')"},
                },
                "required": ["topic"],
            },
        ),
        Tool(
            name="get_prd",
            description=(
                "Get the full content of a specific PRD by name. Use when you need the complete spec, "
                "edge cases, API details, or exact scope of a feature. "
                "Partial name matching works — e.g. 'unpledge optimisations' will find the right PRD."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "PRD name or partial name"},
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="find_related",
            description=(
                "Find all PRDs semantically connected to a given PRD — using both the knowledge graph "
                "(conceptual relationships, part-of hierarchies) and explicit content mentions. "
                "Use this to understand the full scope of a feature area or find enhancements built on top of a flow."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "PRD name to find connections for"},
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="list_topics",
            description="List all available topic summaries with PRD counts. Use this to understand what topic areas exist.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="get_graph_summary",
            description=(
                "Get a high-level summary of the entire knowledge graph — most connected PRDs (god nodes), "
                "community clusters, and key abstractions. Use this to understand the overall structure of the "
                "product knowledge base, or to find the most central/influential PRDs."
            ),
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:

    if name == "search":
        query = arguments["query"]
        limit = int(arguments.get("limit", 5))
        results = fts_search(query, limit)
        return [TextContent(type="text", text=format_search_results(results, query))]

    elif name == "get_topic":
        topic = arguments["topic"].lower().strip()
        summary_file = SUMMARIES_PATH / f"{topic}.md"
        if summary_file.exists():
            return [TextContent(type="text", text=summary_file.read_text())]
        available = [f.stem for f in SUMMARIES_PATH.glob("*.md")] if SUMMARIES_PATH.exists() else []
        matches = [t for t in available if topic in t or t in topic]
        if matches:
            return [TextContent(type="text", text=(SUMMARIES_PATH / f"{matches[0]}.md").read_text())]
        topic_list = ", ".join(available) if available else "none built yet"
        return [TextContent(type="text", text=f"Topic **\"{topic}\"** not found.\n\nAvailable topics: {topic_list}")]

    elif name == "get_prd":
        name_q = arguments["name"]
        row = get_file_by_name(name_q)
        if not row:
            results = fts_search(name_q, limit=3)
            if results:
                suggestions = "\n".join(f"- {r['title']}" for r in results)
                return [TextContent(type="text", text=
                    f"PRD **\"{name_q}\"** not found.\n\nDid you mean:\n{suggestions}\n\n"
                    f"Try `search` with a broader term."
                )]
            return [TextContent(type="text", text=f"PRD **\"{name_q}\"** not found. Try `search` to locate it.")]
        return [TextContent(type="text", text=format_prd(row))]

    elif name == "find_related":
        name_q = arguments["name"]
        row = get_file_by_name(name_q)
        if not row:
            return [TextContent(type="text", text=f"PRD **\"{name_q}\"** not found.")]

        title = row["title"]
        lines = [f"## Related PRDs for: {title}\n"]

        # --- Knowledge graph relationships (graphify) ---
        graph_related = _graph.get_related(title)
        if graph_related:
            by_relation: dict[str, list[tuple[str, str]]] = {}
            no_index: list[str] = []
            for r in graph_related:
                if r["in_index"]:
                    fp = _graph.get_filepath(r["label"])
                    abs_fp = str(ROOT / fp) if fp else ""
                    by_relation.setdefault(r["relation"], []).append((r["label"], abs_fp))
                else:
                    no_index.append(r["label"])

            lines.append("### Knowledge graph (semantic relationships):")
            for rel, entries in by_relation.items():
                rel_display = rel.replace("_", " ").title()
                lines.append(f"\n**{rel_display}:**")
                for label, abs_fp in entries:
                    path_str = f"\n    `{abs_fp}`" if abs_fp else ""
                    lines.append(f"  - {label}{path_str}")

            if no_index:
                lines.append(f"\n*Also connected (not in local index): {', '.join(no_index[:5])}*")
        elif _graph.loaded:
            lines.append("*This PRD has no connections in the knowledge graph.*\n")
        else:
            lines.append("*Knowledge graph not available (graphify-out/graph.json missing).*\n")

        # --- Index-based: files that explicitly mention this PRD ---
        mentions = get_mentions_from_index(title)
        if mentions:
            lines.append("\n\n### PRDs that reference this:")
            for r in mentions:
                abs_fp = str(ROOT / r["file_path"]) if r.get("file_path") else ""
                lines.append(
                    f"- **{r['title']}** — {r.get('status') or '—'} | last edited: {r.get('last_edited') or '—'}\n"
                    f"  `{abs_fp}`"
                )

        if not graph_related and not mentions:
            lines.append("No related PRDs found.")

        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "list_topics":
        from _build import get_all_topics
        topics = get_all_topics()
        if not topics:
            return [TextContent(type="text", text="No topic summaries built yet. Run `python3 setup.py` to build them.")]
        lines = ["## Available Topic Summaries\n"]
        for t in topics:
            lines.append(f"- **{t['topic']}** — {t['prd_count']} PRDs")
        lines.append("\n*Use `get_topic` with any topic name above.*")
        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "get_graph_summary":
        if GRAPH_REPORT.exists():
            content = GRAPH_REPORT.read_text()
            # Strip Obsidian wikilinks for readability in Claude
            content = re.sub(r'\[\[([^\]|]+)\|?([^\]]*)\]\]', lambda m: m.group(2) or m.group(1), content)
            return [TextContent(type="text", text=content)]
        if not GRAPH_JSON.exists():
            return [TextContent(type="text", text=
                "Knowledge graph not available. The `graphify-out/` directory is not present in this repo clone."
            )]
        # Fallback: compute basic stats from graph.json
        data = json.loads(GRAPH_JSON.read_text())
        node_count = len(data["nodes"])
        edge_count = len(data["links"])
        communities = len(set(n.get("community", 0) for n in data["nodes"]))
        # Find most connected nodes
        degree: dict[str, int] = {}
        for link in data["links"]:
            degree[link["source"]] = degree.get(link["source"], 0) + 1
            degree[link["target"]] = degree.get(link["target"], 0) + 1
        node_map = {n["id"]: n["label"] for n in data["nodes"]}
        top = sorted(degree.items(), key=lambda x: -x[1])[:10]
        lines = [
            f"## Knowledge Graph Summary\n",
            f"- **{node_count} nodes** · **{edge_count} edges** · **{communities} communities**\n",
            "### Most connected PRDs (god nodes):",
        ]
        for i, (nid, deg) in enumerate(top, 1):
            lines.append(f"{i}. **{node_map.get(nid, nid)}** — {deg} connections")
        return [TextContent(type="text", text="\n".join(lines))]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main():
    ensure_index()
    _graph.load()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
