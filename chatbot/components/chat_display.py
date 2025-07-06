import streamlit as st
from utils.session_utils import get_current_chat_history, add_message
from utils.prompt_utils import build_context_prompt
from utils.llm_utils import generate_response

def render_chat():
    history = get_current_chat_history()

    if len(history) == 0:
        st.markdown("""
        <div style="text-align: center; margin-top: 100px; color: #d1d5db;">
            <h1 style="font-weight: 600; font-size: 28px;">How can I help you today? 🤖</h1>
            <p style="font-size: 16px; color: #9ca3af;">Ask me anything — whether it’s code, math, writing, or just curiosity.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")  # spacer

    # Show previous chat messages
    for msg in history:
        avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Message ChatGPT...")
    if user_input:
        st.chat_message("user", avatar="🧑‍💻").markdown(user_input)
        add_message("user", user_input)

        with st.spinner(""):
            prompt = build_context_prompt(history, user_input)
            response = generate_response(prompt)
            st.chat_message("assistant", avatar="🤖").markdown(response)
            add_message("assistant", response)
