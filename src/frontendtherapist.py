import streamlit as st
from therapist import get_response

st.set_page_config(page_title="Therapist Bot", page_icon="🧠")

st.title("🐄 Mr.Moo")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.history = []

# Display chat messages from history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input for user message
if prompt := st.chat_input("How are you feeling today?"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from therapist bot
    response, updated_history = get_response(prompt, st.session_state.history)
    st.session_state.history = updated_history

    # Display therapist response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
