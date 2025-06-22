import streamlit as st
from app import ask_ai, df
from main import addlogo

addlogo()

st.set_page_config(page_title="Mooody - Homepage", page_icon="photos/justcow_logo.png")

st.title("Welcome to Mooody!")
