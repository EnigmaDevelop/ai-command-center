# src/tools/__init__.py

from .calculator import calculate
# CORRECTED: We are now importing the function named 'web_request'
from .web_request import web_request

# We are centralizing our tools in a dictionary for easy access.
# The agent's system prompt refers to the tool as "web_request".
# We map that string name to the actual function we just imported.
AVAILABLE_TOOLS = {
    "calculate": calculate,
    # CORRECTED: The key "web_request" now maps to the 'web_request' function.
    "web_request": web_request,
}
