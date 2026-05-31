<div align="center">

# 🧠 Volt PRDs — Knowledge Agent

**Ask anything about Volt Money / DSP Finance product flows — right inside Claude Code.**

Powered by 760+ PRDs, full-text search, topic summaries, and a semantic knowledge graph.

</div>

---

## ✨ What it does

Type `/volt` in Claude Code and ask naturally:

```
How does the pledge flow work today?
What is the current KYC process for DSP?
Show me the mandate registration PRD
How do we perform bulk unlink collateral for LAMF?
What is the STP logic for sell-off repayment reconciliation?
What changed recently in repayment?
```

Claude pulls answers directly from the actual PRDs — no hallucinations, no stale memory.

---

## 🚀 Setup

**Requirements:** Python 3.10+, [Claude Code](https://claude.ai/code) installed.

### 1. Clone

```bash
git clone https://github.com/coder-glitche/volt_product_knowlege_agent.git
cd volt_product_knowlege_agent
```

### 2. Download the Product Repository

Download **`Product Repository.zip`** and place it in the repo folder:

> 📦 **[Download Product Repository.zip](https://drive.google.com/file/d/1HNzRUyJEmuHOo-1vquCnpFjA23wxzEbD/view?usp=drive_link)**

```
volt_product_knowlege_agent/
└── Product Repository.zip   ← place it here
```

### 3. Run setup

```bash
python3 setup.py
```

This will:
- Extract `Product Repository.zip`
- Install dependencies
- Build the search index (SQLite FTS5)
- Build topic summaries
- Register the MCP server with Claude Code
- Install the `/volt` slash command

### 3. Use the agent

> In a new terminal Restart Claude Code** once setup completes, then type `/volt` to activate.
```
claude /volt
```

---

## 🔄 Keeping it up to date

Drop new `.md` files into `Product Repository/` and run:

```bash
python3 setup.py --refresh
```

Refresh a single topic for a quicker update:

```bash
python3 setup.py --refresh --topic pledge
```

<details>
<summary>Available topics</summary>

`pledge` · `mandate` · `kyc` · `repayment` · `disbursement` · `foreclosure` · `loan-origination` · `loan-management` · `comms` · `ops-tools` · `b2b` · `mfd` · `analytics` · `compliance` · `credit-limit` · `collections`

</details>

> **Fresh clone?** If you don't have the `Product Repository/` folder yet, just place the zip in the repo root before running `--refresh` — it will be extracted automatically.

---

## 🛠️ How it works

```
Your question
     │
     ▼
 /volt mode
     │
     ├── get_topic    → pre-built summary of a topic area (newest PRD first)
     ├── search       → BM25 full-text search across all 760+ PRDs
     ├── get_prd      → full content of a specific PRD
     ├── find_related → knowledge graph + explicit content mentions
     ├── list_topics  → all topic areas with PRD counts
     └── get_graph_summary → most connected PRDs and community clusters
```

- **Search index** — SQLite FTS5 with BM25 ranking, built from all markdown files
- **Topic summaries** — synthesised from all PRDs per topic, newest first, pre-committed so Claude can answer without re-reading everything
- **Knowledge graph** — semantic relationships inferred across PRDs via graphify; surfaces `conceptually_related_to` and `part_of` connections in `find_related`

No external APIs. Runs entirely on your machine.

---

## 📁 Repo structure

```
volt_product_knowlege_agent/
├── knowledge/
│   └── summaries/      # pre-built topic summaries (committed to git)
├── setup.py            # one-command setup & refresh
├── server.py           # MCP server — 6 tools
├── _build.py           # indexer + summariser (called by setup.py)
└── requirements.txt
```

> `Product Repository/` and `Product Repository.zip` are **never committed** — they stay on your local machine only.  
> `knowledge/index.db` is generated locally and not committed.
