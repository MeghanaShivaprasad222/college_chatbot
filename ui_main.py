# main.py (for Streamlit UI)

import streamlit as st
from router import route_query  # This uses the backend logic you already wrote

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Info Chatbot")
st.markdown("Ask me anything about your college life — events, academics, admissions, hostel, and more!")

# Input box for user query
query = st.text_input("Type your question here:", "")

# Button to submit
if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = route_query(query)
            st.success(response)
