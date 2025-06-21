from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline
import csv
from huggingface_hub import login
from datetime import date
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("HF_TOKEN")


login(token)

emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores = True)

log = input("Journal Log: ")

emotion_labels = emotion(log)
print(emotion_labels)

date = date.today()
emotion_scores = {item['label']: item['score'] for item in emotion_labels[0]}
anger = emotion_scores['anger']
disgust = emotion_scores['disgust']
fear = emotion_scores['fear']
joy = emotion_scores['joy']
neutral = emotion_scores['neutral']
sadness = emotion_scores['sadness']
surprise = emotion_scores['surprise']

happiness_score = anger*1 + disgust*4 + fear*2 + joy*10 + neutral*5 +sadness*1 + surprise*6

data = [date, anger, disgust, fear, joy, neutral, sadness, surprise, happiness_score, log]

columns = ["Date", "Anger_Score","Disgust_Score","Fear_Score","Joy_Score","Neutral_Score","Sadness_Score","Surprise_Score","Happiness_Score", "Text"]

df = pd.DataFrame([data], columns = columns)