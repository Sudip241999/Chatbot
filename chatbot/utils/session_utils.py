import streamlit as st

def init_session():
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = {"New Chat": []}
    if "current_chat" not in st.session_state:
        st.session_state.current_chat = "New Chat"

def get_current_chat_history():
    return st.session_state.chat_sessions[st.session_state.current_chat]

def add_message(role, content):
    st.session_state.chat_sessions[st.session_state.current_chat].append({
        "role": role,
        "content": content
    })

def create_new_chat():
    # Don't create new chat if current one is still empty
    current_history = st.session_state.chat_sessions.get(st.session_state.current_chat, [])
    if len(current_history) == 0:
        return  # Do nothing

    chat_num = len(st.session_state.chat_sessions) + 1
    name = f"Chat {chat_num}"
    st.session_state.chat_sessions[name] = []
    st.session_state.current_chat = name

def delete_chat(name):
    if name in st.session_state.chat_sessions:
        del st.session_state.chat_sessions[name]

        # If no chats remain after deletion, create a new one
        if not st.session_state.chat_sessions:
            st.session_state.chat_sessions["New Chat"] = []
            st.session_state.current_chat = "New Chat"
        else:
            # Switch to the first available chat
            st.session_state.current_chat = list(st.session_state.chat_sessions.keys())[0]


def rename_chat(old_name, new_name):
    if old_name in st.session_state.chat_sessions:
        st.session_state.chat_sessions[new_name] = st.session_state.chat_sessions.pop(old_name)
