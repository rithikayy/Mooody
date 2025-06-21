import streamlit as st
from main import analyzelog
import pandas as pd
from google import genai
from google.genai import types


def ask_ai(df):
   data_frame = df.sort_values(by='Date') 
   if not data_frame.empty:
       latest_entry = data_frame.iloc[-1]['Text']
   else:
       latest_entry = "No journal entries yet."

   new_q = latest_entry + "Ask a question based on this journal entry. Keep it open-ended and be specific! If it's empty or not much content, just ask a basic open-ended question like 'how's your day?' BE STRAIGHTFORWARD AND BRIEF"

   response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents=new_q,
       config=types.GenerateContentConfig(
           thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
       ),
   )
   return response.text

client = genai.Client(api_key="AIzaSyApoB8gTGfRy4UotGrIdgwcrfeLgKmep0g")

columns = ["Date", "Anger_Score","Disgust_Score","Fear_Score","Joy_Score","Neutral_Score","Sadness_Score","Surprise_Score","Happiness_Score", "Text"]

df = pd.DataFrame(columns=columns)

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
with st.container():
   st.title("Welcome to Mooody!")

if "visibility" not in st.session_state:
   st.session_state.visibility = "visible"
   st.session_state.disabled = False

ai_question = ask_ai(df)
text_input = st.text_input(
       ai_question,
       label_visibility=st.session_state.visibility,
       disabled=st.session_state.disabled,
   )

pg = st.navigation([
   st.Page(page2, title="SecondPage", icon=":material/favorite:"),
])

pg.run()

# if text_input:
#    data_row = analyzelog(text_input)
#    new_row = pd.DataFrame([data_row], columns=df.columns)
#    df = pd.concat([df, new_row], ignore_index=True)
#    df['Date'] = pd.to_datetime(df['Date'])
#    st.subheader("Happiness Score Over Time")
#    st.line_chart(df.set_index('Date')['Happiness_Score'])
