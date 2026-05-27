#!/usr/bin/env python3
"""
Volt PRDs MCP Server
Exposes the graphify knowledge graph of Volt Money PRDs as MCP tools for Claude Code.
"""

import json
import os
from collections import defaultdict
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

# ---------------------------------------------------------------------------
# Resolve data path
# ---------------------------------------------------------------------------

def _resolve_graphify_path() -> Path:
    env = os.environ.get("GRAPHIFY_PATH")
    if env:
        p = Path(env)
    else:
        p = Path(__file__).parent / "graphify-out"
    if not p.exists():
        raise RuntimeError(
            f"graphify-out not found at {p}.\n"
            "Set GRAPHIFY_PATH env var or place graphify-out/ next to server.py.\n"
            "See README.md for setup instructions."
        )
    return p


# ---------------------------------------------------------------------------
# Load graph and build indices at startup
# ---------------------------------------------------------------------------

class Graph:
    def __init__(self, graphify_path: Path):
        self.path = graphify_path
        self.obsidian_path = graphify_path / "obsidian"
        self.report_path = graphify_path / "GRAPH_REPORT.md"

        data = json.loads((graphify_path / "graph.json").read_text())
        nodes = data["nodes"]
        links = data["links"]

        # label (lowercase) -> node
        self.label_index: dict[str, dict] = {
            n["label"].lower(): n for n in nodes
        }
        # original-case label list for search display
        self.labels: list[str] = [n["label"] for n in nodes]

        # community id -> [nodes]
        self.community_index: dict[int, list[dict]] = defaultdict(list)
        for n in nodes:
            self.community_index[n["community"]].append(n)

        # node id -> node
        self.id_index: dict[str, dict] = {n["id"]: n for n in nodes}

        # adjacency: node id -> list of {label, relation, confidence_score}
        self.adj: dict[str, list[dict]] = defaultdict(list)
        for link in links:
            src, tgt = link["source"], link["target"]
            self.adj[src].append({
                "label": self.id_index.get(tgt, {}).get("label", tgt),
                "relation": link["relation"],
                "confidence_score": link.get("confidence_score", 0),
            })
            self.adj[tgt].append({
                "label": self.id_index.get(src, {}).get("label", src),
                "relation": link["relation"],
                "confidence_score": link.get("confidence_score", 0),
            })

    def fuzzy_find(self, name: str) -> dict | None:
        """Return best matching node for a name string."""
        key = name.lower().strip()
        if key in self.label_index:
            return self.label_index[key]
        # substring match
        matches = [(l, n) for l, n in self.label_index.items() if key in l]
        if matches:
            matches.sort(key=lambda x: len(x[0]))
            return matches[0][1]
        return None

    def read_obsidian(self, label: str) -> str | None:
        f = self.obsidian_path / f"{label}.md"
        return f.read_text() if f.exists() else None


# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

server = Server("volt-prds")
graph: Graph | None = None


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_prds",
            description="Search PRDs by keyword. Returns matching PRD names, their community, and source path.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search term (case-insensitive substring match on PRD name)"},
                    "limit": {"type": "integer", "description": "Max results to return (default 10)", "default": 10},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="get_prd",
            description="Get the full content and connections of a specific PRD by name.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "PRD name (exact or partial match)"},
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="find_related",
            description="Find all PRDs directly connected to a given PRD in the knowledge graph, with relation types.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "PRD name to find connections for"},
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="list_communities",
            description="List all topic communities in the PRD graph with member counts and sample PRD names.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="get_community",
            description="Get all PRDs in a specific community cluster.",
            inputSchema={
                "type": "object",
                "properties": {
                    "community_id": {"type": "integer", "description": "Community number (0–36)"},
                },
                "required": ["community_id"],
            },
        ),
        Tool(
            name="get_graph_summary",
            description="Get the high-level graph report: god nodes, community overview, knowledge gaps, and suggested questions.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    assert graph is not None

    if name == "search_prds":
        query = arguments["query"].lower()
        limit = int(arguments.get("limit", 10))
        matches = [
            (label, node)
            for label, node in graph.label_index.items()
            if query in label
        ]
        matches.sort(key=lambda x: (not x[0].startswith(query), len(x[0])))
        matches = matches[:limit]

        if not matches:
            return [TextContent(type="text", text=f"No PRDs found matching '{arguments['query']}'.")]

        lines = [f"Found {len(matches)} PRD(s) matching '{arguments['query']}':\n"]
        for _, node in matches:
            lines.append(
                f"- **{node['label']}**\n"
                f"  Community: {node['community']} | "
                f"Type: {node.get('file_type', 'unknown')}\n"
                f"  Source: {node.get('source_file', 'N/A')}"
            )
        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "get_prd":
        node = graph.fuzzy_find(arguments["name"])
        if not node:
            return [TextContent(type="text", text=f"PRD '{arguments['name']}' not found. Try search_prds to find the exact name.")]

        content = graph.read_obsidian(node["label"])
        if content:
            return [TextContent(type="text", text=content)]

        # Fallback: return node metadata
        return [TextContent(type="text", text=
            f"# {node['label']}\n\n"
            f"- Community: {node['community']}\n"
            f"- Source: {node.get('source_file', 'N/A')}\n"
            f"- Type: {node.get('file_type', 'unknown')}\n\n"
            f"*(Obsidian file not found — obsidian/ folder may be missing)*"
        )]

    elif name == "find_related":
        node = graph.fuzzy_find(arguments["name"])
        if not node:
            return [TextContent(type="text", text=f"PRD '{arguments['name']}' not found. Try search_prds to find the exact name.")]

        connections = graph.adj.get(node["id"], [])
        if not connections:
            return [TextContent(type="text", text=f"No connections found for '{node['label']}'.")]

        connections_sorted = sorted(connections, key=lambda x: -x["confidence_score"])
        lines = [f"## Connections for: {node['label']}\n"]
        by_relation: dict[str, list[str]] = defaultdict(list)
        for c in connections_sorted:
            by_relation[c["relation"]].append(c["label"])
        for relation, labels in by_relation.items():
            lines.append(f"**{relation}:**")
            for label in labels:
                lines.append(f"  - {label}")
        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "list_communities":
        lines = ["# Volt PRDs — Community Overview\n"]
        lines.append(f"Total: {len(graph.community_index)} communities\n")
        for cid in sorted(graph.community_index.keys()):
            nodes = graph.community_index[cid]
            if not nodes:
                continue
            sample = [n["label"] for n in nodes[:4]]
            more = len(nodes) - 4
            sample_str = ", ".join(sample)
            if more > 0:
                sample_str += f" (+{more} more)"
            lines.append(f"**Community {cid}** ({len(nodes)} PRDs): {sample_str}")
        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "get_community":
        cid = int(arguments["community_id"])
        # Try reading obsidian community file first
        community_file = graph.obsidian_path / f"_COMMUNITY_Community {cid}.md"
        if community_file.exists():
            return [TextContent(type="text", text=community_file.read_text())]

        # Fallback: build from index
        nodes = graph.community_index.get(cid, [])
        if not nodes:
            return [TextContent(type="text", text=f"Community {cid} not found.")]
        lines = [f"# Community {cid} ({len(nodes)} PRDs)\n"]
        for n in nodes:
            lines.append(f"- {n['label']}")
        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "get_graph_summary":
        if graph.report_path.exists():
            return [TextContent(type="text", text=graph.report_path.read_text())]
        return [TextContent(type="text", text="GRAPH_REPORT.md not found in graphify-out/.")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main():
    global graph
    graphify_path = _resolve_graphify_path()
    graph = Graph(graphify_path)

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
