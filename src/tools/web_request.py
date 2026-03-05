import requests

def fetch_url(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Only show first 500 chars to avoid huge output
        return response.text[:500]

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
