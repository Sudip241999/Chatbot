import streamlit as st
from streamlit_supabase_auth import login_form, logout_button
from supabase_config import init_supabase

def login_ui():
    supabase = init_supabase()
    session = login_form(
        url=st.secrets["SUPABASE_URL"],
        apiKey=st.secrets["SUPABASE_ANON_KEY"],
        providers=["google"],
    )
    if session:
        user = session["user"]
        st.session_state["user_email"] = user["email"]
        return True
    return False

def logout_ui():
    st.sidebar.button("Logout", on_click=lambda: st.session_state.clear())
