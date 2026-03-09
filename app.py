# app.py

import streamlit as st
# Import the agent function from our source package
from src.agent import run_agent

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Command Center",
    page_icon="🤖",
    layout="centered",
)

# --- PAGE TITLE ---
st.title("🤖 AI Command Center")
st.caption("Your intelligent agent powered by Ollama Server-llama2 and Streamlit")


# --- SESSION STATE INITIALIZATION ---
# Streamlit apps re-run from top to bottom on every user interaction.
# To remember the conversation history, we store it in `st.session_state`.
# We initialize it here if it doesn't already exist.
if "messages" not in st.session_state:
    st.session_state.messages = []


# --- DISPLAY CHAT HISTORY ---
# This loop runs every time the app re-renders, displaying the full chat history.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --- HANDLE USER INPUT ---
# `st.chat_input` creates a text input field at the bottom of the page.
# When the user types something and presses Enter, the code inside the `if` block runs.
if prompt := st.chat_input("Ask your agent anything... (e.g., 'What is 5*12?' or 'Get me the contents of https://www.google.com')"):

    # 1. Add user's message to the chat history and display it.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get the agent's response.
    with st.chat_message("assistant"):
        # Show a "Thinking..." spinner while the agent is working.
        with st.spinner("Thinking..."):
            # This is where we call our new, intelligent agent function!
            # We pass the user's prompt and the entire conversation history.
            response = run_agent(prompt, st.session_state.messages)
            st.markdown(response)

    # 3. Add the agent's response to the chat history.
    st.session_state.messages.append({"role": "assistant", "content": response})

