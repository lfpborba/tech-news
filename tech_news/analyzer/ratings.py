from tech_news.database import find_news


# Requisito 10
def top_5_news():
    sorted_news = sorted(find_news(), key=lambda n: n['comments_count'],
                         reverse=True)

    return [(new["title"], new["url"]) for new in sorted_news[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
