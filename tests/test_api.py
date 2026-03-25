from unittest.mock import patch, Mock
import requests
import api


@patch("api.requests.get")
def test_fetch_quotes_success(mock_get):
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: [{"text": "Be happy.", "author": "Someone"}],
    )
    mock_get.return_value.raise_for_status = Mock()

    result = api.fetch_quotes()
    assert len(result) == 1
    assert result[0]["text"] == "Be happy."


@patch("api.requests.get", side_effect=requests.Timeout)
def test_fetch_quotes_timeout(mock_get):
    result = api.fetch_quotes()
    assert result == []


@patch("api.requests.get", side_effect=requests.ConnectionError)
def test_fetch_quotes_connection_error(mock_get):
    result = api.fetch_quotes()
    assert result == []


@patch("api.fetch_quotes")
def test_get_random_quote_from_api_success(mock_fetch):
    mock_fetch.return_value = [{"text": "Stay strong.", "author": "Jane"}]
    result = api.get_random_quote_from_api()
    assert result["quote"] == "Stay strong."
    assert result["author"] == "Jane"


@patch("api.fetch_quotes")
def test_get_random_quote_from_api_null_author(mock_fetch):
    mock_fetch.return_value = [{"text": "Hello world.", "author": None}]
    result = api.get_random_quote_from_api()
    assert result["author"] == "Unknown"


@patch("api.fetch_quotes")
def test_get_random_quote_from_api_empty(mock_fetch):
    mock_fetch.return_value = []
    result = api.get_random_quote_from_api()
    assert result is None
