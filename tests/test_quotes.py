from quotes import MOOD_QUOTES, get_quote_for_mood


def test_all_moods_have_quotes():
    expected_moods = {
        "happy", "sad", "mad", "angry", "frustrated",
        "anxious", "stressed", "lonely", "tired",
        "hopeful", "grateful", "motivated",
    }
    assert set(MOOD_QUOTES.keys()) == expected_moods


def test_each_mood_has_at_least_six_quotes():
    for mood, quotes in MOOD_QUOTES.items():
        assert len(quotes) >= 6, f"{mood} has only {len(quotes)} quotes"


def test_quote_structure():
    for mood, quotes in MOOD_QUOTES.items():
        for q in quotes:
            assert "quote" in q, f"{mood}: missing 'quote' key"
            assert "author" in q, f"{mood}: missing 'author' key"
            assert isinstance(q["quote"], str) and q["quote"]
            assert isinstance(q["author"], str) and q["author"]


def test_get_quote_for_mood_returns_dict():
    result = get_quote_for_mood("happy")
    assert isinstance(result, dict)
    assert "quote" in result
    assert "author" in result


def test_get_quote_for_mood_unknown_returns_none():
    assert get_quote_for_mood("nonexistent") is None
