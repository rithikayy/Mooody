import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.logo("cowlogo.jpeg", size="large")

st.title("Data Dashboard 🚀")
st.write("by Arav :3")


# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# data_frame = pd.read_csv(uploaded_file)

# data_frame = pd.read_csv('journal_entries.csv')

# do something like this...but replace data with your own
data = {
    'Date': ['2025-06-01', '2025-06-02'],
    'Anger': [3.5, 2.0],
    'Disgust': [1.0, 3.5],
    'Fear': [2.0, 1.0],
    'Joy': [0, 0],
    'Neutral': [0, 0],
    'Sadness': [0, 0],
    'Surprise': [0, 0],
    'Text': ["Felt great today!", "Bit anxious, not sure."],
    'Happiness Score': [0.93, 0.62]
}
data_frame = pd.DataFrame(data)
data_frame['Date'] = pd.to_datetime(data_frame['Date'])  



st.subheader("Filter data")
columns = data_frame.columns.tolist()
selected_column = st.selectbox("Select column to filter by", columns)
unique_values = data_frame[selected_column].unique()
selected_value = st.selectbox("Selected values", unique_values)


filtered_data = data_frame[data_frame[selected_column] == selected_value]
st.write(filtered_data)

st.markdown("""
<style>
span[data-baseweb="tag"]:has(span[title="Anger"]) {
  color: white;
  background-color: light-red;
}

span[data-baseweb="tag"]:has(span[title="Disgust"]) {
  color: white;
  background-color: #3CB371;
}

span[data-baseweb="tag"]:has(span[title="Fear"]) {
  color: white;
  background-color: #DDA0DD;
}
            
span[data-baseweb="tag"]:has(span[title="Joy"]) {
  color: white;
  background-color: orange;
}
            
span[data-baseweb="tag"]:has(span[title="Neutral"]) {
  color: white;
  background-color: grey;
}
            
span[data-baseweb="tag"]:has(span[title="Sadness"]) {
  color: white;
  background-color: #6495ED;
}
            
span[data-baseweb="tag"]:has(span[title="Surprise"]) {
  color: white;
  background-color: #48D1CC;
}
</style>
""", unsafe_allow_html=True)

st.subheader("Plot data")
emotions_col = st.multiselect("Select emotions to plot", ["Anger", "Disgust", "Fear", "Joy", "Neutral", "Sadness", "Surprise"]) # emotions, maybe multiselect?


if st.button("Generate Plot"):
    st.line_chart(data_frame.set_index('Date')[emotions_col])


#happiness score chart
st.subheader("Happiness Score Over Time")
st.line_chart(data_frame.set_index('Date')['Happiness Score'])