# src/tools/web_request.py

import requests
from bs4 import BeautifulSoup

def web_request(url: str) -> str:
    """
    Fetches the clean text content of a given URL.

    Args:
        url: The URL to fetch content from. Must be a full URL (e.g., https://...).

    Returns:
        A string containing the clean text of the webpage, or an error message.
    """
    try:
        # Add a user-agent to mimic a browser and prevent being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Use BeautifulSoup to parse HTML and get only the text
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)

        # Return only the first 2000 characters to avoid overwhelming the LLM
        return clean_text[:2000] + "..." if len(clean_text) > 2000 else clean_text

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL {url}: {e}"
    except Exception as e:
        return f"An unexpected error occurred while processing the webpage: {e}"

