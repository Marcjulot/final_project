import requests

API_URL = "https://zenquotes.io/api/random"


def get_random_quote_from_api():
    """Return a single random quote from ZenQuotes as {"quote": ..., "author": ...}."""
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        if not data:
            return None
        pick = data[0]
        return {
            "quote": pick.get("q", ""),
            "author": pick.get("a") or "Unknown",
        }
    except (requests.ConnectionError, requests.Timeout, requests.HTTPError, ValueError):
        return None
