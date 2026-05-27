# Volt PRDs — MCP Server

Query the entire Volt Money PRD knowledge graph directly inside Claude Code. Ask Claude to find PRDs by topic, explore how documents are connected, or pull up any specific PRD — without leaving your session.

---

## Prerequisites

- Python 3.10 or later (`python3 --version`)
- pip (`pip3 --version`)
- Claude Code installed and working

---

## Setup (3 steps)

### 1. Clone this repo

```bash
git clone https://github.com/voltmoney/volt-prds-mcp.git
cd volt-prds-mcp
```

### 2. Add the graphify-out folder

The PRD data is not stored in this repo. Copy or move your `graphify-out/` folder so it sits next to `server.py`:

```
volt-prds-mcp/
├── server.py
├── requirements.txt
├── README.md
└── graphify-out/        ← place it here
    ├── graph.json
    ├── GRAPH_REPORT.md
    └── obsidian/
```

> If you store `graphify-out/` somewhere else, set the env var `GRAPHIFY_PATH=/path/to/graphify-out` in your Claude Code settings (see step 3).

### 3. Install dependencies

```bash
pip3 install -r requirements.txt
```

---

## Add to Claude Code

Run this command (replace the path with your actual clone location):

```bash
claude mcp add --scope user volt-prds \
  -- python3 /absolute/path/to/volt-prds-mcp/server.py
```

**If graphify-out is in a custom location** (not next to server.py), pass it as an env var:

```bash
claude mcp add --scope user volt-prds \
  -e GRAPHIFY_PATH="/absolute/path/to/graphify-out" \
  -- python3 /absolute/path/to/volt-prds-mcp/server.py
```

Verify it's connected:

```bash
claude mcp list
# volt-prds: python3 ... - ✓ Connected
```

---

## Available tools

Once connected, Claude can use these tools automatically when you ask questions about the PRDs.

| Tool | What it does | Example prompt |
|---|---|---|
| `search_prds` | Find PRDs by keyword | *"Find all PRDs related to mandate"* |
| `get_prd` | Get full content of a PRD | *"Show me the Term Loan Disbursement PRD"* |
| `find_related` | See connected PRDs and how they relate | *"What is connected to Mandate registration post loan?"* |
| `list_communities` | Browse all 37 topic clusters | *"What topic clusters exist in the PRD graph?"* |
| `get_community` | Get all PRDs in a cluster | *"Show me everything in community 28"* |
| `get_graph_summary` | High-level graph report and key nodes | *"Give me a summary of the PRD knowledge graph"* |

### Example prompts to try

```
Find all PRDs about foreclosure
Show me the KYC Hub PRD
What PRDs are connected to UPI Autopay?
Which community covers Term Loans?
What are the most connected PRDs in the graph?
Find PRDs related to DSP mandate
Show me community 3
```

---

## Updating the PRD data

When new PRDs are added or graphify is re-run:

1. Re-run graphify on the Volt Product vault to regenerate `graphify-out/`
2. Replace the `graphify-out/` folder next to `server.py` with the new one
3. Restart Claude Code — the server reloads on the next session

No code changes needed.

---

## Troubleshooting

**"graphify-out not found" error**
- Check that `graphify-out/` exists next to `server.py`
- Or set `GRAPHIFY_PATH` in the MCP env config pointing to its location

**Server not appearing in Claude Code**
- Confirm the path in `settings.json` is absolute (not relative)
- Run `python3 /path/to/server.py` manually — if it errors, fix that first
- Restart Claude Code fully after editing `settings.json`

**"PRD not found" when using get_prd**
- Use `search_prds` first to find the exact PRD name
- Partial matches work: `"mandate registration"` will find `"Mandate registration post loan"`

**Tools not being called automatically**
- Claude won't always call tools unless prompted. Be explicit: *"Use the volt-prds tools to find..."*
- Or just ask naturally and Claude will decide when to call them

---

## How it works

The server loads `graphify-out/graph.json` (751 nodes, 1963 edges across 37 communities) at startup and builds in-memory indices. Tool calls are served from memory with file reads for full PRD content. No network calls, no external dependencies beyond the `mcp` package.
