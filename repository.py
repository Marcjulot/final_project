import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "list.db"


def get_random_quote():
    """Return a random quote from the database as a dict."""
    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute(
            "SELECT quote, author FROM quotes ORDER BY RANDOM() LIMIT 1"
        ).fetchone()
        if row:
            return {"quote": row[0], "author": row[1]}
        return {"quote": "Stay positive!", "author": "Unknown"}
    finally:
        conn.close()


def get_all_quotes():
    """Return all quotes from the database as a list of dicts."""
    conn = sqlite3.connect(DB_PATH)
    try:
        rows = conn.execute("SELECT quote, author FROM quotes").fetchall()
        return [{"quote": r[0], "author": r[1]} for r in rows]
    finally:
        conn.close()
