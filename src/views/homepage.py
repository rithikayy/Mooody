import streamlit as st
from app import ask_ai, df
from main import addlogo

addlogo()

st.set_page_config(page_title="Mooody - Homepage", page_icon="photos/justcow_logo.png")

page_bg_img = '''
<style>
.stApp {
    background-image: url("https://st3.depositphotos.com/28515578/34267/i/450/depositphotos_342675258-stock-photo-epic-dramatic-storm-dark-grey.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Welcome to Mooody! 🐮")
st.text("Moody is an interactive mental health journaling web app developed by Arav, Angelin, Rithika, and Valence. Designed to promote emotional well-being, Moody allows users to reflect on their thoughts and track their mental health over time through daily journaling. At its core is Mr. Moo, an empathetic AI-powered therapist chatbot who offers supportive, conversational interactions to help users better understand and process their emotions.")
st.text("Moody features mood tracking that visually displays changes in emotional states across time, encouraging self-awareness and growth. With a friendly interface and meaningful AI interaction, Moody provides a safe digital space for users to express themselves, build healthy mental habits, and feel supported—one entry at a time.")
