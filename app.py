import streamlit as st
import requests

st.title("News Summarization & Sentiment Analysis")

company = st.text_input("Enter company name:")

if st.button("Analyze"):
    response = requests.get(f"http://127.0.0.1:8000/get_news/{company}").json()
    for article in response:
        st.subheader(article["title"])
        st.write(f"Sentiment: {article['sentiment']}")
