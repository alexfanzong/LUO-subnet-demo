from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LUO Evidence Terminal", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
      .stApp { background: #07090d; }
      .block-container {
        max-width: 100vw;
        padding: 0;
      }
      iframe {
        display: block;
      }
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stStatusWidget"] {
        display: none !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
