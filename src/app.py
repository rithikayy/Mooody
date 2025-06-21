import streamlit as st
from main import analyzelog
import pandas as pd

columns = ["Date", "Anger_Score","Disgust_Score","Fear_Score","Joy_Score","Neutral_Score","Sadness_Score","Surprise_Score","Happiness_Score", "Text"]

df = pd.DataFrame(columns=columns)

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
with st.container():
    st.title("Welcome to Mooody!")

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


text_input = st.text_input(
        "Write about your day 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

if text_input:
    data_row = analyzelog(text_input)
    new_row = pd.DataFrame([data_row], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df['Date'] = pd.to_datetime(df['Date'])
    st.subheader("Happiness Score Over Time")
    st.line_chart(df.set_index('Date')['Happiness_Score'])