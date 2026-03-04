import streamlit as st

st.title("AI Command Center")

user_input = st.text_input("Enter a command:")

if st.button("Run"):

st.write("This is where the agent response will appear.")