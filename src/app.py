import streamlit as st

# Absolute import — your project structure supports this
from src.agent import Agent

# Initialize agent
agent = Agent()

# Streamlit UI
st.title("AI Command Center")

command = st.text_input("Enter a command:")

if st.button("Run"):
    response = agent.run(command)
    st.write(response)
