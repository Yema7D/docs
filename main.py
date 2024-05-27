
import streamlit as st
from pages_.overview import load_overview
from pages_.qlora import load_qlora
from pages_.rag import load_rag
from pages_.fine_tunning import load_fine_tuning


# Dictionary to map button names to page-loading functions
pages = {
    "Overview": load_overview,
    "QLoRA":load_qlora,
    "Fine-Tuning": load_fine_tuning,
    "RAG" : load_rag
}

# Sidebar buttons to switch pages
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
pages[selection](st)