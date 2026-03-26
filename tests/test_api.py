from unittest.mock import patch, Mock
import requests
import api


@patch("api.requests.get")
def test_get_random_quote_success(mock_get):
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: [{"q": "Be happy.", "a": "Someone"}],
    )
    mock_get.return_value.raise_for_status = Mock()

    result = api.get_random_quote_from_api()
    assert result["quote"] == "Be happy."
    assert result["author"] == "Someone"


@patch("api.requests.get", side_effect=requests.Timeout)
def test_get_random_quote_timeout(mock_get):
    result = api.get_random_quote_from_api()
    assert result is None


@patch("api.requests.get", side_effect=requests.ConnectionError)
def test_get_random_quote_connection_error(mock_get):
    result = api.get_random_quote_from_api()
    assert result is None


@patch("api.requests.get")
def test_get_random_quote_null_author(mock_get):
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: [{"q": "Hello world.", "a": None}],
    )
    mock_get.return_value.raise_for_status = Mock()

    result = api.get_random_quote_from_api()
    assert result["author"] == "Unknown"


@patch("api.requests.get")
def test_get_random_quote_empty_response(mock_get):
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: [],
    )
    mock_get.return_value.raise_for_status = Mock()

    result = api.get_random_quote_from_api()
    assert result is None
