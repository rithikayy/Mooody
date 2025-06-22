import streamlit as st
from app import analyzelog
from app import add_to_df
from main import addlogo
from app import ask_ai, df

addlogo()

st.title("Journal")

question = ask_ai(df)

# user_input = st.text_input(question)

text_input = st.text_area(question, height=200)

if text_input:
   data_row = analyzelog(text_input)
   add_to_df(data_row, df)
   