import requests
from bs4 import BeautifulSoup
from newspaper import Article

def fetch_news_links(company):
    """Fetches 10 news article links related to the given company."""
    search_url = f"https://news.google.com/search?q={company}&hl=en"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("article")[:10]:  # Limit to 10 articles
        title_tag = item.find("h3")
        if title_tag:
            title = title_tag.text
            link = f"https://news.google.com{item.find('a')['href']}"
            articles.append({"title": title, "link": link})

    return articles

def extract_article_content(url):
    """Extracts the article text from the given URL using Newspaper3k."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text[:500]  # Limit to 500 characters for summarization
    except:
        return "Content not available."


