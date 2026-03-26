from unittest.mock import patch
from positivoquotes import format_quote, MOOD_RESPONSES, ALL_MOODS


def test_format_quote():
    q = {"quote": "Be yourself.", "author": "Oscar Wilde"}
    assert format_quote(q) == '"Be yourself." — Oscar Wilde'


def test_all_moods_have_required_keys():
    for mood, entry in MOOD_RESPONSES.items():
        assert "message" in entry, f"{mood} missing 'message'"
        assert "encouragement" in entry, f"{mood} missing 'encouragement'"


def test_mood_responses_contains_all_twelve_moods():
    expected = {
        "happy", "sad", "mad", "angry", "frustrated",
        "anxious", "stressed", "lonely", "tired",
        "hopeful", "grateful", "motivated",
    }
    assert set(MOOD_RESPONSES.keys()) == expected


def test_all_moods_sorted():
    assert ALL_MOODS == sorted(ALL_MOODS)


@patch("positivoquotes.get_quote_for_mood")
@patch("builtins.input", side_effect=["happy", "quit"])
def test_run_happy_then_quit(mock_input, mock_mood_quote, capsys):
    mock_mood_quote.return_value = {"quote": "Smile!", "author": "Test"}
    from positivoquotes import run
    run()
    output = capsys.readouterr().out
    assert "glad" in output
    assert '"Smile!" — Test' in output
    assert "Goodbye" in output


@patch("builtins.input", side_effect=["xyz", "quit"])
def test_run_invalid_mood(mock_input, capsys):
    from positivoquotes import run
    run()
    output = capsys.readouterr().out
    assert "don't recognize" in output


@patch("positivoquotes.get_quote_for_mood")
@patch("builtins.input", side_effect=["anxious", "quit"])
def test_run_new_mood_anxious(mock_input, mock_mood_quote, capsys):
    mock_mood_quote.return_value = {"quote": "Breathe.", "author": "Guru"}
    from positivoquotes import run
    run()
    output = capsys.readouterr().out
    assert "anxious" in output.lower() or "overwhelming" in output.lower()
    assert '"Breathe." — Guru' in output
