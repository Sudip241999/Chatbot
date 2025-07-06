import streamlit as st

def inject_custom_css():
    with open("styles/theme.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
