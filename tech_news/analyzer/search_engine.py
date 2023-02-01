from tech_news.database import search_news
from datetime import datetime

# Requisito 6
def search_by_title(title):
    news = []
    news_searched = search_news({"title": {"$regex": title, "$options": "i"}})

    for new in news_searched:
        data = (new["title"], new["url"])
        news.append(data)

    return news


# Requisito 7
def search_by_date(date):
        try:
        news = []
        date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_searched = search_news({"timestamp": {"$eq": date}})

        for new in news_searched:
            news.append((new["title"], new["url"]))

        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = []
    news_searched = search_news({"tags": {"$regex": tag, "$options": "i"}})
    
    for new in news_searched:
        news.append((new["title"], new["url"]))

    return news


# Requisito 9
def search_by_category(category):
    news = []
    news_searched = search_news({"category": {"$regex": category, "$options": "i"}})

    for new in news_searched:
        news.append((new["title"], new["url"]))

    return news
