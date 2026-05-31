#!/usr/bin/env python3
"""
setup.py — One command to set up or refresh the Volt PRDs knowledge agent.

First time setup (after placing Product Repository.zip in this folder):
    python3 setup.py

Refresh after updating Product Repository.zip with new PRDs:
    python3 setup.py --refresh

Refresh a specific topic only:
    python3 setup.py --refresh --topic pledge
"""

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT         = Path(__file__).resolve().parent
PYTHON       = sys.executable
SERVER       = ROOT / "server.py"
REQ          = ROOT / "requirements.txt"
KNOWLEDGE    = ROOT / "knowledge"
DB_PATH      = KNOWLEDGE / "index.db"
PRODUCT_REPO = ROOT / "Product Repository"
REPO_ZIP     = ROOT / "Product Repository.zip"
SLASH_CMD    = Path.home() / ".claude" / "commands" / "volt.md"

SLASH_CMD_CONTENT = """\
You are now in Volt PRDs mode. A `volt-prds` MCP server is available with the full Volt Money / DSP Finance product knowledge base.

For every question in this session, use the volt-prds tools to answer:

- "How does X work" or "what is the current system for X" → call `get_topic` with the relevant topic (pledge, mandate, kyc, repayment, disbursement, foreclosure, loan-origination, loan-management, comms, ops-tools, b2b, mfd, analytics, compliance, credit-limit, collections)
- "Show me the X PRD" or "what does X PRD say" → call `get_prd`
- "What's related to / connected to X" → call `find_related`
- Any other product question → call `search`

Always use the volt-prds tools first. Do not rely on memory or codebase for product questions.

Acknowledge by saying "Volt PRDs mode active — what do you want to know?" and wait for the user's question.
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run(cmd: list, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def resolve_python() -> str:
    venv_py = ROOT / ".venv" / "bin" / "python3"
    return str(venv_py) if venv_py.exists() else PYTHON


def step(msg: str):
    print(f"\n→ {msg}")


def ok(msg: str):
    print(f"  ✓ {msg}")


def fail(msg: str):
    print(f"  ✗ {msg}")


# ---------------------------------------------------------------------------
# Setup steps
# ---------------------------------------------------------------------------

def extract_repo(force: bool = False):
    """Extract Product Repository.zip if the folder is missing or force=True."""
    if not REPO_ZIP.exists():
        if PRODUCT_REPO.exists():
            return  # folder already there, nothing to do
        fail("Product Repository.zip not found.")
        print(f"\n  Place 'Product Repository.zip' in:\n    {ROOT}\n  then re-run setup.py.\n")
        sys.exit(1)

    if PRODUCT_REPO.exists() and not force:
        md_count = len(list(PRODUCT_REPO.rglob("*.md")))
        ok(f"Product Repository already extracted ({md_count} markdown files)")
        return

    step("Extracting Product Repository.zip...")
    import shutil
    if PRODUCT_REPO.exists():
        shutil.rmtree(PRODUCT_REPO)
    with zipfile.ZipFile(REPO_ZIP, "r") as zf:
        zf.extractall(ROOT)
    md_count = len(list(PRODUCT_REPO.rglob("*.md")))
    ok(f"Extracted ({md_count} markdown files)")


def install_deps():
    step("Installing dependencies...")
    result = run([PYTHON, "-m", "pip", "install", "-r", str(REQ)], check=False)
    if result.returncode != 0:
        venv_pip = ROOT / ".venv" / "bin" / "pip"
        if not venv_pip.exists():
            print("  Creating virtual environment...")
            run([PYTHON, "-m", "venv", str(ROOT / ".venv")])
        run([str(ROOT / ".venv" / "bin" / "pip"), "install", "-r", str(REQ)])
    ok("Dependencies ready")


def build_index(verbose: bool = True):
    step("Building search index from Product Repository...")
    sys.path.insert(0, str(ROOT))
    from _build import build_index as _build
    count = _build(verbose=verbose)
    ok(f"{count} files indexed")


def build_summaries(topic: str = None, verbose: bool = True):
    step("Building topic summaries...")
    sys.path.insert(0, str(ROOT))

    if topic:
        from _build import TOPICS, SUMMARIES_PATH, extract_section
        import sqlite3
        if topic not in TOPICS:
            fail(f"Unknown topic '{topic}'. Available: {', '.join(TOPICS.keys())}")
            return
        SUMMARIES_PATH.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        rows = conn.execute(
            "SELECT title, file_path, status, last_edited, content "
            "FROM files WHERE topic_areas LIKE ? ORDER BY last_edited DESC",
            (f"%{topic}%",)
        ).fetchall()
        conn.close()
        lines = [
            f"# Current State: {topic.replace('-', ' ').title()}",
            f"\n> Auto-generated from {len(rows)} PRD(s). Most recently edited shown first.\n",
        ]
        for i, (title, file_path, status, last_edited, content) in enumerate(rows):
            tag = "🟢 LATEST" if i == 0 else f"#{i+1}"
            lines.append(f"\n---\n\n## {tag} — {title}")
            lines.append(f"**Status:** {status or 'Unknown'} | **Last edited:** {last_edited or 'Unknown'}")
            problem  = extract_section(content, r'#{1,3}\s+\*?\*?What problem')
            solution = extract_section(content, r'#{1,3}\s+\*?\*?What is the solution')
            if problem:  lines.append(f"\n**Problem:**\n{problem[:600]}")
            if solution: lines.append(f"\n**Solution:**\n{solution[:800]}")
            if not (problem or solution):
                lines.append("\n" + " ".join(content.split()[:400]))
        (SUMMARIES_PATH / f"{topic}.md").write_text("\n".join(lines))
        ok(f"Refreshed: {topic} ({len(rows)} PRDs)")
    else:
        from _build import build_summaries as _build_summaries
        count = _build_summaries(verbose=verbose)
        ok(f"{count} topic summaries built")


def register_mcp():
    step("Registering MCP server with Claude Code...")
    py = resolve_python()
    run(["claude", "mcp", "remove", "volt-prds"], check=False)
    result = run(["claude", "mcp", "add", "--scope", "user", "volt-prds", "--", py, str(SERVER)])
    if result.returncode == 0:
        ok("MCP server registered")
    else:
        fail(f"MCP registration failed: {result.stderr.strip()}")
        print(f"  Run manually: claude mcp add --scope user volt-prds -- {py} {SERVER}")


def install_slash_command():
    step("Installing /volt slash command...")
    SLASH_CMD.parent.mkdir(parents=True, exist_ok=True)
    SLASH_CMD.write_text(SLASH_CMD_CONTENT)
    ok(f"/volt command installed → {SLASH_CMD}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Set up or refresh the Volt PRDs knowledge agent.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 setup.py                          # first-time setup
  python3 setup.py --refresh                # re-extract zip + rebuild after new PRDs
  python3 setup.py --refresh --topic pledge # refresh one topic summary only
        """
    )
    parser.add_argument("--refresh", action="store_true",
                        help="Re-extract zip and rebuild index + summaries")
    parser.add_argument("--topic", type=str, default=None,
                        help="Refresh a specific topic summary only (use with --refresh)")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress per-file output")
    args = parser.parse_args()

    verbose = not args.quiet

    print("\n🔧 Volt PRDs Knowledge Agent\n")

    if args.refresh:
        extract_repo(force=True)
        build_index(verbose)
        build_summaries(topic=args.topic, verbose=verbose)
        print("\n✅ Refresh complete. Restart Claude Code to pick up changes.\n")
    else:
        install_deps()
        extract_repo(force=False)
        build_index(verbose)
        build_summaries(verbose=verbose)
        register_mcp()
        install_slash_command()
        print("\n✅ All done!\n")
        print("  1. Restart Claude Code")
        print("  2. Type /volt to activate the knowledge agent")
        print("  3. Ask anything about Volt / DSP product flows\n")


if __name__ == "__main__":
    main()
