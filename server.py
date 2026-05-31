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
        # BM25 ranked FTS search
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
        # Fallback to LIKE search if FTS fails
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
    # Exact title match
    row = conn.execute(
        "SELECT * FROM files WHERE lower(title) = ?", (name_l,)
    ).fetchone()
    if not row:
        # Substring match, shortest title wins
        rows = conn.execute(
            "SELECT * FROM files WHERE lower(title) LIKE ? ORDER BY length(title)",
            (f"%{name_l}%",)
        ).fetchall()
        row = rows[0] if rows else None
    conn.close()
    return dict(row) if row else None


def get_related_from_index(title: str, limit: int = 8) -> list[dict]:
    """Find files that mention this title or share most topic areas."""
    conn = get_db()
    title_l = title.lower()
    # Files that mention this PRD's title in their content
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


def get_graphify_related(label: str) -> list[dict] | None:
    """Use graphify graph for related PRDs if available."""
    graph_json = GRAPHIFY_PATH / "graph.json"
    if not graph_json.exists():
        return None
    try:
        data = json.loads(graph_json.read_text())
        nodes = {n["id"]: n for n in data["nodes"]}
        label_to_id = {n["label"].lower(): n["id"] for n in data["nodes"]}
        node_id = label_to_id.get(label.lower())
        if not node_id:
            return None
        related = []
        for link in data["links"]:
            if link["source"] == node_id:
                target = nodes.get(link["target"], {})
                related.append({"label": target.get("label", ""), "relation": link["relation"]})
            elif link["target"] == node_id:
                source = nodes.get(link["source"], {})
                related.append({"label": source.get("label", ""), "relation": link["relation"]})
        return related[:10]
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Format helpers
# ---------------------------------------------------------------------------

def format_search_results(results: list[dict], query: str) -> str:
    if not results:
        return f"No results found for **\"{query}\"**."

    lines = [f"## Search results for \"{query}\"\n"]
    for i, r in enumerate(results, 1):
        topics = r.get("topic_areas", "").replace(",", " · ")
        lines.append(
            f"### {i}. {r['title']}\n"
            f"**Topics:** {topics}  |  **Status:** {r.get('status') or '—'}  |  **Last edited:** {r.get('last_edited') or '—'}\n\n"
            f"{r.get('snippet', '').strip()}\n"
        )
    lines.append(f"\n*Use `get_prd` with a title above for the full document.*")
    return "\n".join(lines)


def format_prd(row: dict) -> str:
    file_path = ROOT / row["file_path"]
    if file_path.exists():
        content = file_path.read_text(errors="ignore")
        # Strip base64 images
        content = re.sub(r'!\[.*?\]\(data:image/[^)]+\)', '[image removed]', content)
        return content
    # Fallback to indexed content
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
                "Find all PRDs connected to a given PRD — other specs that reference it, "
                "enhancements built on top of it, or related flows. "
                "Use this to understand the full scope of a feature area."
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
        # Fuzzy: find closest topic
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
            # Try search as fallback
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

        # Try graphify graph first
        graph_related = get_graphify_related(title)
        if graph_related:
            by_relation: dict[str, list[str]] = {}
            for r in graph_related:
                by_relation.setdefault(r["relation"], []).append(r["label"])
            lines.append("### From knowledge graph:")
            for rel, labels in by_relation.items():
                lines.append(f"\n**{rel}:**")
                for label in labels:
                    lines.append(f"  - {label}")

        # Index-based: files that mention this PRD
        index_related = get_related_from_index(title)
        if index_related:
            lines.append("\n\n### PRDs that reference this:")
            for r in index_related:
                lines.append(
                    f"- **{r['title']}** — {r.get('status') or '—'} | last edited: {r.get('last_edited') or '—'}"
                )

        if not graph_related and not index_related:
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

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main():
    ensure_index()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
