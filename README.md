# Volt PRDs — Knowledge Agent

Query the entire Volt Money / DSP Finance product knowledge base directly inside Claude Code. Ask about any feature, flow, PRD, or system — and get accurate answers sourced from the actual product repository.

---

## Setup

**Requirements:** Python 3.10+, Claude Code installed.

### 1. Clone the repo

```bash
git clone https://github.com/coder-glitche/volt_product_knowlege_agent.git
cd volt_product_knowlege_agent
```

### 2. Download the Product Repository

Download **Product Repository.zip** from the link below and place it in the repo folder:

> **[Download Product Repository.zip](YOUR_GOOGLE_DRIVE_LINK_HERE)**

```
volt_product_knowlege_agent/
└── Product Repository.zip   ← place it here
```

### 3. Run setup

```bash
python3 setup.py
```

Setup will:
- Extract `Product Repository.zip`
- Install dependencies
- Build the search index
- Build topic summaries
- Register the MCP server with Claude Code
- Install the `/volt` slash command

**Restart Claude Code** once setup completes.

---

## Usage

Type `/volt` in any Claude Code session to activate the knowledge agent:

```
/volt
```

Then ask anything naturally:

```
How does the pledge flow work today?
What is the current KYC process for DSP?
Show me the mandate registration PRD
What changed recently in repayment?
How do we perform bulk unlink collateral for LAMF?
What is the STP logic for sell-off repayment reconciliation?
```

---

## Keeping it up to date

Just drop new markdown files into the `Product Repository/` folder and run:

```bash
# Reindex everything
python3 setup.py --refresh

# Reindex a specific topic only (faster)
python3 setup.py --refresh --topic pledge
```

If you don't have the folder yet (fresh clone), place `Product Repository.zip` in the repo root first — `--refresh` will extract it automatically.

Available topics: `pledge`, `mandate`, `kyc`, `repayment`, `disbursement`, `foreclosure`, `loan-origination`, `loan-management`, `comms`, `ops-tools`, `b2b`, `mfd`, `analytics`, `compliance`, `credit-limit`, `collections`

---

## Repo structure

```
volt_product_knowlege_agent/
├── knowledge/
│   └── summaries/          # Pre-built topic summaries (committed)
├── setup.py                # One-command setup & refresh
├── server.py               # MCP server (6 tools)
├── _build.py               # Indexer and summariser (internal)
└── requirements.txt
```

`Product Repository/` and `Product Repository.zip` are never committed — they live only on your local machine.  
`knowledge/index.db` is generated locally on setup and is not committed.

---

## How it works

- `setup.py` extracts the zip, scans all markdown files, builds a SQLite full-text search index (BM25), and generates per-topic "current state" summaries ordered by last edited date.
- A knowledge graph (`graphify-out/graph.json`) maps semantic relationships between PRDs — used by `find_related` to surface conceptually connected specs.
- The MCP server exposes 6 tools that Claude Code calls automatically in `/volt` mode:

| Tool | Use |
|---|---|
| `search` | Full-text search across all PRDs |
| `get_topic` | Current state summary for a topic area |
| `get_prd` | Full content of a specific PRD |
| `find_related` | Semantic + explicit connections to a PRD |
| `list_topics` | All available topic areas with counts |
| `get_graph_summary` | Knowledge graph overview and god nodes |

No external APIs. Everything runs locally.
