from unittest.mock import patch
from positivoquotes import format_quote, MOOD_RESPONSES, run


def test_format_quote():
    q = {"quote": "Be yourself.", "author": "Oscar Wilde"}
    assert format_quote(q) == '"Be yourself." — Oscar Wilde'


def test_all_moods_have_required_keys():
    for mood, entry in MOOD_RESPONSES.items():
        assert "message" in entry, f"{mood} missing 'message'"
        assert "encouragement" in entry, f"{mood} missing 'encouragement'"


def test_mood_responses_contains_expected_moods():
    expected = {"happy", "sad", "mad", "angry", "frustrated"}
    assert set(MOOD_RESPONSES.keys()) == expected


@patch("positivoquotes.get_random_quote")
@patch("builtins.input", side_effect=["happy", "quit"])
def test_run_happy_then_quit(mock_input, mock_quote, capsys):
    mock_quote.return_value = {"quote": "Smile!", "author": "Test"}
    run()
    output = capsys.readouterr().out
    assert "glad" in output
    assert '"Smile!" — Test' in output
    assert "Goodbye" in output


@patch("builtins.input", side_effect=["xyz", "quit"])
def test_run_invalid_mood(mock_input, capsys):
    run()
    output = capsys.readouterr().out
    assert "don't recognize" in output
