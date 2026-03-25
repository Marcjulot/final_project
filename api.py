import random
import requests

API_URL = "https://type.fit/api/quotes"


def fetch_quotes():
    """Fetch quotes from the API. Returns a list of dicts or [] on failure."""
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except (requests.ConnectionError, requests.Timeout, requests.HTTPError, ValueError):
        return []


def get_random_quote_from_api():
    """Return a single random quote from the API as {"quote": ..., "author": ...}."""
    quotes = fetch_quotes()
    if not quotes:
        return None
    pick = random.choice(quotes)
    return {
        "quote": pick.get("text", ""),
        "author": pick.get("author") or "Unknown",
    }
