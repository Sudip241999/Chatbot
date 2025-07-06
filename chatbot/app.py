import streamlit as st
from components.sidebar import render_sidebar
from components.chat_display import render_chat
from utils.session_utils import init_session
from styles.theme import inject_custom_css
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

st.set_page_config(page_title="AskMebaby", layout="wide", page_icon="🤖")


inject_custom_css()
init_session()
render_sidebar()
render_chat()
