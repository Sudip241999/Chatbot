import streamlit as st
from utils.session_utils import (
    create_new_chat,
    rename_chat,
    delete_chat,
)

def render_sidebar():
    with st.sidebar:
        st.markdown("### 💬 AskMeBabyyy")

        if st.button("➕ New Chat", use_container_width=True):
            create_new_chat()

        st.markdown("---")
        st.markdown("<div style='color: #8e8ea0; font-size: 14px;'>Chat History</div>", unsafe_allow_html=True)

        # Scrollable container for chat history
        st.markdown("""
        <style>
            .scrollable-chat {
                max-height: 500px;
                overflow-y: auto;
                padding-right: 5px;
            }
            .chat-item-btn {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background: transparent;
                border: none;
                width: 100%;
                text-align: left;
                color: white;
                padding: 6px 10px;
                border-radius: 6px;
                margin-bottom: 4px;
            }
            .chat-item-btn:hover {
                background-color: #2b2c2f;
            }
        </style>
        <div class='scrollable-chat'>
        """, unsafe_allow_html=True)

        for name in list(st.session_state.chat_sessions.keys()):
            is_active = name == st.session_state.current_chat

            col1, col2, col3 = st.columns([6, 1, 1])
            with col1:
                if st.button(f"💬 {name}", key=f"chat-{name}", use_container_width=True):
                    st.session_state.current_chat = name
            with col2:
                if st.button("✏️", key=f"rename-{name}", help="Rename Chat", use_container_width=True):
                    st.session_state.rename_target = name
            with col3:
                if st.button("🗑️", key=f"delete-{name}", help="Delete Chat", use_container_width=True):
                    st.session_state.delete_target = name

        st.markdown("</div>", unsafe_allow_html=True)

        # Rename Chat Modal
        if "rename_target" in st.session_state:
            with st.form("rename_form", clear_on_submit=True):
                new_name = st.text_input("Rename chat", st.session_state.rename_target)
                submitted = st.form_submit_button("Rename")
                if submitted and new_name:
                    rename_chat(st.session_state.rename_target, new_name)
                    st.session_state.current_chat = new_name
                    del st.session_state.rename_target
                    st.rerun()

        # Delete Chat Confirmation
        if "delete_target" in st.session_state:
            st.warning(f"Are you sure you want to delete '{st.session_state.delete_target}'?")
            col_del1, col_del2 = st.columns(2)
            with col_del1:
                if st.button("❌ Yes, Delete"):
                    delete_chat(st.session_state.delete_target)
                    del st.session_state.delete_target
                    st.rerun()
            with col_del2:
                if st.button("Cancel"):
                    del st.session_state.delete_target
