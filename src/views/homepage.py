import streamlit as st
from app import ask_ai, df

st.title("Welcome to Mooody!")

question = ask_ai(df)

user_input = st.text_input(question)