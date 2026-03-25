import sqlite3
import repository


def _create_test_db(tmp_path):
    """Create a temporary test database with sample quotes."""
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE quotes (quote_id int, quote text, author text)")
    conn.execute(
        "INSERT INTO quotes VALUES (1, 'Be yourself.', 'Oscar Wilde')"
    )
    conn.execute(
        "INSERT INTO quotes VALUES (2, 'Stay hungry.', 'Steve Jobs')"
    )
    conn.commit()
    conn.close()
    return db_path


def test_get_random_quote(tmp_path, monkeypatch):
    db_path = _create_test_db(tmp_path)
    monkeypatch.setattr(repository, "DB_PATH", db_path)

    quote = repository.get_random_quote()
    assert "quote" in quote
    assert "author" in quote
    assert quote["quote"] in ("Be yourself.", "Stay hungry.")


def test_get_all_quotes(tmp_path, monkeypatch):
    db_path = _create_test_db(tmp_path)
    monkeypatch.setattr(repository, "DB_PATH", db_path)

    quotes = repository.get_all_quotes()
    assert len(quotes) == 2
    assert quotes[0]["author"] in ("Oscar Wilde", "Steve Jobs")


def test_get_random_quote_empty_db(tmp_path, monkeypatch):
    db_path = tmp_path / "empty.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE quotes (quote_id int, quote text, author text)")
    conn.commit()
    conn.close()
    monkeypatch.setattr(repository, "DB_PATH", db_path)

    quote = repository.get_random_quote()
    assert quote == {"quote": "Stay positive!", "author": "Unknown"}
