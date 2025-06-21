import streamlit as st
from app import analyzelog
from app import add_to_df

st.title("Journal")

text_input = st.text_area("Enter your journal entry here:", height=200)

if text_input:
   data_row = analyzelog(text_input)
   add_to_df(data_row)
   