# src/agent.py

import os
import json
from dotenv import load_dotenv
import ollama

from .tools import AVAILABLE_TOOLS

# --- INITIALIZATION ---
load_dotenv()

# Model configuration
MODEL_NAME = "llama2"  # Using llama2 which is already installed. Change to "mistral" if you pull it.
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

try:
    # Test connection to Ollama
    test_client = ollama.Client(host=OLLAMA_HOST)
    test_client.list()
    print(f"[OK] Connected to Ollama at {OLLAMA_HOST}")
except Exception as e:
    print(f"[WARNING] Could not connect to Ollama at {OLLAMA_HOST}")
    print("Please ensure Ollama is running: https://ollama.ai")
    print("The app will attempt to use Ollama when needed.")

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = """You are a helpful AI assistant. Your role is to understand the user's request and assist them.
You have access to a set of tools to get information or perform tasks.
**You should interpret the user's request, even if it is not in English, and use the appropriate tool.**

Based on the user's prompt, you must decide on one of two actions:
1.  **Answer directly:** If the user's question is a general query or a conversational remark that you can answer from your own knowledge, provide a direct, helpful response.
2.  **Use a tool:** If the user's request requires specific information (like a real-time web search) or a specific capability (like a calculation), you must use one of the available tools.

**Available Tools:**
- `calculate(expression: str)`: Use this for any mathematical calculation. Example: `2*(3+5)/4`
- `web_request(url: str)`: Use this to get the content of a webpage. Example: `https://www.google.com`

**TOOL USAGE FORMAT:**
When you decide to use a tool, you MUST respond ONLY with the following XML-like format. Do not add any other text or explanation before or after the tag.

<tool>tool_name(argument)</tool>

**Examples:**
- User asks: "What is 12 plus 5 times 8?"
- Your response: <tool>calculate(12+5*8)</tool>
"""

def run_agent(prompt: str, chat_history: list) -> str:
    """
    Runs the AI agent for a single turn using Ollama.
    """
    # --- CONVERT HISTORY ---
    messages = []
    
    # Add system prompt as the first message
    messages.append({
        'role': 'user',
        'content': SYSTEM_PROMPT
    })
    messages.append({
        'role': 'assistant',
        'content': 'Understood. I am ready to assist.'
    })
    
    # Add the existing chat history from Streamlit's session state
    for message in chat_history:
        role = "user" if message["role"] == "user" else "assistant"
        messages.append({
            'role': role,
            'content': message["content"]
        })
    
    try:
        # --- SEND MESSAGE TO OLLAMA ---
        client = ollama.Client(host=OLLAMA_HOST)
        response = client.chat(model=MODEL_NAME, messages=messages)
        response_text = response['message']['content'].strip()
        
        # --- TOOL PARSING AND EXECUTION ---
        if response_text.startswith("<tool>") and response_text.endswith("</tool>"):
            tool_call_string = response_text[6:-7]
            try:
                tool_name, arg_part = tool_call_string.split("(", 1)
                argument = arg_part[:-1] 
            except ValueError:
                return f"Error: Invalid tool format received: {response_text}"
    
            print(f"[Agent] Using tool: {tool_name} with argument: '{argument}'")
    
            if tool_name in AVAILABLE_TOOLS:
                tool_function = AVAILABLE_TOOLS[tool_name]
                tool_result = tool_function(argument)
                return str(tool_result)
            else:
                return f"Error: The model tried to use a tool named '{tool_name}' which does not exist."
        else:
            return response_text
    
    except Exception as e:
        print(f"An error occurred while running the agent: {e}")
        return "Sorry, an error occurred while I was processing your request. Please check the terminal for details."

