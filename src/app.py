import streamlit as st
from main import analyzelog
import pandas as pd
from google import genai
from google.genai import types

columns = ["Date", "Anger","Disgust","Fear","Joy","Neutral","Sadness","Surprise","Happiness Score", "Text"]

df = pd.DataFrame(columns=columns) 

def add_to_df(data):
    new_row = pd.DataFrame([data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)

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

home_page = st.Page(
    "views/homepage.py",
    title="Welcome to Mooody!"
)
project_1_page = st.Page(
    "views/journal.py",
    title="Journal"
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
)
project_3_page = st.Page(
    "views/mood_dashboard.py",
    title = "Mood Dashboard"
)

pg = st.navigation([home_page, project_1_page, project_2_page, project_3_page])

pg.run()

# if text_input:
#    data_row = analyzelog(text_input)
#    new_row = pd.DataFrame([data_row], columns=df.columns)
#    df = pd.concat([df, new_row], ignore_index=True)
#    df['Date'] = pd.to_datetime(df['Date'])
#    st.subheader("Happiness Score Over Time")
#    st.line_chart(df.set_index('Date')['Happiness_Score'])
