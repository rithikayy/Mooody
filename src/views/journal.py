import streamlit as st
from app import analyzelog
from app import add_to_df
from main import addlogo
from app import ask_ai, df

addlogo()
st.set_page_config(page_title="Mooody - Journal", page_icon="photos/justcow_logo.png")
st.title("Journal")

question = ask_ai(df)

# user_input = st.text_input(question)

text_input = st.text_area(question, height=200)

if st.button("Submit Entry"):
   data_row = analyzelog(text_input)
   if data_row is not None:
      add_to_df(data_row, df)
      st.success("Entry added!")
   