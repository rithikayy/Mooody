from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline
import csv
from huggingface_hub import login
from datetime import date
import os
import streamlit as st
from dotenv import load_dotenv
from therapist import get_response

load_dotenv()

def analyzelog(text):
    emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores = True)

    emotion_labels = emotion(text)

    today_date = date.today()
    emotion_scores = {item['label']: item['score'] for item in emotion_labels[0]}
    anger = emotion_scores['anger']
    disgust = emotion_scores['disgust']
    fear = emotion_scores['fear']
    joy = emotion_scores['joy']
    neutral = emotion_scores['neutral']
    sadness = emotion_scores['sadness']
    surprise = emotion_scores['surprise']

    happiness_score = anger*1 + disgust*4 + fear*2 + joy*10 + neutral*5 +sadness*1 + surprise*6

    data = [today_date, anger, disgust, fear, joy, neutral, sadness, surprise, happiness_score, text]

    return data

def addlogo():
    options = ["photos/justcow_logo.png", "photos/newlogo.png"]
    sidebar_logo = options[1]
    main_body_logo = options[0]
    st.logo(sidebar_logo, size="large", icon_image=main_body_logo)


if __name__ == "__main__":
    print("Chatbot started. Type 'exit' to quit.")
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        response, history = get_response(user_input, history)
        print("Therapist:", response)


