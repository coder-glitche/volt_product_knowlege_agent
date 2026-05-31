# Volt PRDs — Knowledge Agent

Query the entire Volt Money / DSP Finance product knowledge base directly inside Claude Code. Ask about any feature, flow, PRD, or system — and get accurate answers sourced from the actual product repository.

---

## Setup

**Requirements:** Python 3.10+, Claude Code installed.

```bash
git clone https://github.com/vaibs-hash/volt-prds-mcp.git
cd volt-prds-mcp
python3 setup.py
```

That's it. Setup will:
- Install dependencies
- Build the search index from the Product Repository
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

After pulling new PRDs into the `Product Repository/` folder:

```bash
# Rebuild everything
python3 setup.py --refresh

# Rebuild a specific topic only
python3 setup.py --refresh --topic pledge
```

Available topics: `pledge`, `mandate`, `kyc`, `repayment`, `disbursement`, `foreclosure`, `loan-origination`, `loan-management`, `comms`, `ops-tools`, `b2b`, `mfd`, `analytics`, `compliance`, `credit-limit`, `collections`

---

## Adding new PRDs

1. Export PRDs from Notion as **Markdown & CSV** (include subpages)
2. Drop the exported folder into `Product Repository/`
3. Run `python3 setup.py --refresh`
4. Restart Claude Code

---

## Repo structure

```
volt-prds-mcp/
├── Product Repository/     # Source PRDs (Notion markdown export)
├── knowledge/
│   └── summaries/          # Pre-built topic summaries (committed)
├── setup.py                # One-command setup & refresh
├── server.py               # MCP server
├── _build.py               # Indexer and summariser (internal)
└── requirements.txt
```

`knowledge/index.db` is generated locally on setup and is not committed — it's built from the PRDs on your machine.

---

## How it works

- `setup.py` scans all markdown files in `Product Repository/`, builds a SQLite full-text search index, and generates per-topic "current state" summaries ordered by last edited date.
- The MCP server exposes 5 tools (`search`, `get_topic`, `get_prd`, `find_related`, `list_topics`) that Claude Code calls automatically when you're in `/volt` mode.
- No external APIs. Everything runs locally.
