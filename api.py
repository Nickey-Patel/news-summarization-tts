from fastapi import FastAPI
from news_scraper import fetch_news_links, extract_article_content
from sentiment_analysis import analyze_sentiment
from tts_hindi import generate_audio

app = FastAPI()

@app.get("/get_news/{company}")
def get_news(company: str):
    """Fetches news articles and performs sentiment analysis."""
    news = fetch_news_links(company)
    
    for article in news:
        content = extract_article_content(article["link"])
        article["summary"] = content
        article["sentiment"] = analyze_sentiment(content)

    return news

@app.get("/generate_audio/{company}")
def get_audio(company: str):
    """Generates Hindi speech summarizing news sentiment."""
    summary = f"{company} ke news ka vishleshan diya ja raha hai."  # Placeholder summary
    filename = generate_audio(summary)
    return {"audio_file": filename}
