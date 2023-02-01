from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    sorted_news = sorted(find_news(), key=lambda n: n['comments_count'],
                         reverse=True)

    return [(new["title"], new["url"]) for new in sorted_news[:5]]


# Requisito 11
def top_5_categories():
    results = find_news()
    categories = [news["category"] for news in results]
    categories.sort()
    counted = Counter(categories)
    top_categories = [c[0] for c in counted.most_common()]

    return top_categories[:5]
