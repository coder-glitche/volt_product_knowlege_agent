"""
Internal module — not meant to be run directly.
Called by setup.py and server.py to build/refresh the knowledge base.
"""

import re
import json
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRODUCT_REPO = ROOT / "Product Repository"
KNOWLEDGE = ROOT / "knowledge"
DB_PATH = KNOWLEDGE / "index.db"
SUMMARIES_PATH = KNOWLEDGE / "summaries"

CHUNK_SIZE = 500  # words per chunk
CHUNK_OVERLAP = 80

TOPICS = {
    "pledge":          ["pledge", "pledging", "unpledge", "un-pledge", "lien", "revocation", "invocation", "lodg"],
    "mandate":         ["mandate", "nach", "upi autopay", "emandate", "e-mandate", "auto-pay", "autopay"],
    "kyc":             ["kyc", "ckyc", "vkyc", "vcip", "aadhaar", "pan verification", "liveliness", "video kyc"],
    "repayment":       ["repayment", "emi", "overdue", "dues collection", "pay-in", "payin"],
    "disbursement":    ["disbursement", "disburse", "drawdown", "payout"],
    "foreclosure":     ["foreclosure", "foreclose", "sell off", "sell-off", "tos calculation"],
    "loan-origination":["los", "application form", "onboarding", "loan creation", "sanction", "kyc flow", "credit referral"],
    "loan-management": ["lms", "loan account", "loan management", "term loan", "co-lending"],
    "comms":           ["comms", "communication", "sms", "email", "whatsapp", "notification", "template", "dlt"],
    "ops-tools":       ["command centre", "command center", "ops tool", "appsmith", "ops tooling", "maker", "checker"],
    "b2b":             ["b2b", "bajaj", "tata capital", "tcl", "cred", "phonepe", "zype", "jupiter"],
    "mfd":             ["mfd", "mfc", "distributor", "arn", "mutual fund distributor", "mfd channel"],
    "analytics":       ["analytics", "amplitude", "event tracking"],
    "compliance":      ["compliance", "regulatory", "rbi", "credit bureau", "cibil", "bureau reporting"],
    "credit-limit":    ["credit limit", "credit line", "unlock credit", "top-up", "topup", "top up"],
    "collections":     ["collection", "overdue", "npa", "delinquency", "recovery", "dpd"],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_title(path: Path) -> str:
    name = path.stem
    # Strip Notion 32-char hex ID suffix
    clean = re.sub(r'\s+[0-9a-f]{32}$', '', name).strip()
    return clean if clean else name


def extract_metadata(content: str) -> dict:
    meta = {"status": "", "created": "", "last_edited": "", "author": ""}
    m = re.search(r'^:\s*(.+)$', content, re.MULTILINE)
    if m:
        meta["author"] = m.group(1).strip()
    m = re.search(r'Created time:\s*(.+)', content)
    if m:
        meta["created"] = m.group(1).strip()
    m = re.search(r'Last edited:\s*(.+)', content)
    if m:
        meta["last_edited"] = m.group(1).strip()
    m = re.search(r'Status:\s*(.+)', content)
    if m:
        meta["status"] = m.group(1).strip()
    return meta


def extract_section(content: str, heading_pattern: str) -> str:
    """Extract content under a heading until the next heading of same/higher level."""
    match = re.search(heading_pattern, content, re.IGNORECASE)
    if not match:
        return ""
    start = match.end()
    # Find next heading at same or higher level
    next_heading = re.search(r'\n#{1,3} ', content[start:])
    end = start + next_heading.start() if next_heading else start + 2000
    return content[start:end].strip()


def detect_topics(title: str, file_path: Path, content: str) -> list[str]:
    # Match on title + path only to avoid false positives from generic terms in content
    header = (title + " " + str(file_path)).lower()
    matched = []
    for topic, keywords in TOPICS.items():
        if any(kw in header for kw in keywords):
            matched.append(topic)
    # Also derive from folder name
    parts = file_path.parts
    for part in parts:
        p = part.lower()
        if "lms" in p:
            if "loan-management" not in matched:
                matched.append("loan-management")
        if "los" in p:
            if "loan-origination" not in matched:
                matched.append("loan-origination")
        if "mfd" in p:
            if "mfd" not in matched:
                matched.append("mfd")
        if "nbfc" in p:
            pass  # too broad
    return matched or ["general"]


def clean_content(content: str) -> str:
    """Strip base64 images and metadata header from content."""
    # Remove base64 image data
    content = re.sub(r'!\[.*?\]\(data:image/[^)]+\)', '[image]', content)
    # Remove Notion metadata lines at top
    content = re.sub(r'^:\s*.+\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^(Created time|Last edited|Status|Owner|Tasks):.+\n', '', content, flags=re.MULTILINE)
    return content.strip()


def chunk_text(text: str) -> list[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + CHUNK_SIZE])
        chunks.append(chunk)
        i += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


def parse_last_edited(date_str: str) -> datetime:
    for fmt in ("%B %d, %Y %I:%M %p", "%B %d, %Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return datetime.min


# ---------------------------------------------------------------------------
# Index builder
# ---------------------------------------------------------------------------

def build_index(verbose: bool = True) -> int:
    KNOWLEDGE.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript("""
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS files;
        CREATE TABLE files (
            id          INTEGER PRIMARY KEY,
            title       TEXT NOT NULL,
            file_path   TEXT NOT NULL,
            topic_areas TEXT,
            status      TEXT,
            author      TEXT,
            created     TEXT,
            last_edited TEXT,
            word_count  INTEGER,
            content     TEXT
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS files_fts USING fts5(
            title, content, topic_areas,
            content=files, content_rowid=id,
            tokenize='porter ascii'
        );
        CREATE TABLE chunks (
            id          INTEGER PRIMARY KEY,
            file_id     INTEGER REFERENCES files(id),
            chunk_index INTEGER,
            content     TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_chunks_file ON chunks(file_id);
    """)

    md_files = sorted(PRODUCT_REPO.rglob("*.md"))
    count = 0

    for path in md_files:
        try:
            raw = path.read_text(errors="ignore")
        except Exception:
            continue

        title = clean_title(path)
        # Skip index/folder pages (very short, just lists)
        if len(raw.split()) < 30:
            continue

        meta = extract_metadata(raw)
        content = clean_content(raw)
        topics = detect_topics(title, path.relative_to(PRODUCT_REPO), content)
        word_count = len(content.split())

        cur = conn.execute(
            "INSERT INTO files (title, file_path, topic_areas, status, author, created, last_edited, word_count, content) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                title,
                str(path.relative_to(ROOT)),
                ",".join(topics),
                meta["status"],
                meta["author"],
                meta["created"],
                meta["last_edited"],
                word_count,
                content,
            )
        )
        file_id = cur.lastrowid

        for i, chunk in enumerate(chunk_text(content)):
            conn.execute(
                "INSERT INTO chunks (file_id, chunk_index, content) VALUES (?, ?, ?)",
                (file_id, i, chunk)
            )

        count += 1
        if verbose:
            print(f"  indexed: {title[:70]}")

    # Populate FTS index
    conn.execute("INSERT INTO files_fts(files_fts) VALUES('rebuild')")
    conn.commit()
    conn.close()

    if verbose:
        print(f"\n✓ Indexed {count} files → {DB_PATH}")
    return count


# ---------------------------------------------------------------------------
# Summary builder
# ---------------------------------------------------------------------------

def build_summaries(verbose: bool = True) -> int:
    if not DB_PATH.exists():
        raise RuntimeError("Index not built yet. Run build_index() first.")

    SUMMARIES_PATH.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    count = 0

    for topic in TOPICS:
        rows = conn.execute(
            "SELECT title, file_path, status, last_edited, content "
            "FROM files WHERE topic_areas LIKE ? "
            "ORDER BY last_edited DESC",
            (f"%{topic}%",)
        ).fetchall()

        if not rows:
            continue

        lines = [
            f"# Current State: {topic.replace('-', ' ').title()}",
            f"\n> Auto-generated from {len(rows)} PRD(s). Most recently edited shown first.\n",
        ]

        for i, (title, file_path, status, last_edited, content) in enumerate(rows):
            tag = "🟢 LATEST" if i == 0 else f"#{i+1}"
            lines.append(f"\n---\n\n## {tag} — {title}")
            lines.append(f"**Status:** {status or 'Unknown'} | **Last edited:** {last_edited or 'Unknown'}")

            problem = extract_section(content, r'#{1,3}\s+\*?\*?What problem')
            solution = extract_section(content, r'#{1,3}\s+\*?\*?What is the solution')
            scope_in = extract_section(content, r'#{1,3}\s+\*?\*?In scope')

            if problem:
                lines.append(f"\n**Problem:**\n{problem[:600]}")
            if solution:
                lines.append(f"\n**Solution:**\n{solution[:800]}")
            if scope_in:
                lines.append(f"\n**In scope:**\n{scope_in[:400]}")
            if not (problem or solution):
                # Fallback: first 400 words of content
                words = content.split()[:400]
                lines.append("\n" + " ".join(words))

        summary_file = SUMMARIES_PATH / f"{topic}.md"
        summary_file.write_text("\n".join(lines))
        count += 1

        if verbose:
            print(f"  summary: {topic} ({len(rows)} PRDs)")

    conn.close()
    if verbose:
        print(f"\n✓ Built {count} topic summaries → {SUMMARIES_PATH}")
    return count


def get_all_topics() -> list[dict]:
    if not SUMMARIES_PATH.exists():
        return []
    topics = []
    for f in sorted(SUMMARIES_PATH.glob("*.md")):
        topic = f.stem
        content = f.read_text()
        prd_count = content.count("\n## ")
        topics.append({"topic": topic, "prd_count": prd_count, "file": str(f)})
    return topics
