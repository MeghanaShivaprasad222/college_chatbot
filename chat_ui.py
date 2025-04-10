import streamlit as st
from dotenv import load_dotenv
import os
from router import route_query  # Your central LangGraph router function

load_dotenv()

st.set_page_config(page_title="College Chatbot", page_icon="🎓")
st.title("🎓 College Chatbot Assistant")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.chat_input("Ask something about college life...")

if user_input:
    # Add user message to history
    st.session_state.history.append(("You", user_input))

    # Get bot response
    response = route_query(user_input)

    # Add bot response to history
    st.session_state.history.append(("Bot", response))

# Display conversation
for sender, message in st.session_state.history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.write(message)
    