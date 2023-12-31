import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=5, headers={"user-agent": "Fake user-agent"}
        )
        sleep(1)
        response.raise_for_status()

    except (requests.exceptions.HTTPError, requests.exceptions.Timeout):
        return

    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = [a.attrib["href"] for a in selector.css(".post-inner h2 a")]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    new_link = Selector(text=html_content)
    next_link = new_link.css(".next::attr(href)").get()
    if next_link:
        return next_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    results = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date ::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(
            selector.css("div.comment-body").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text")
            .getall()
        ).strip(),
        "tags": selector.css("[rel=tag]::text").getall(),
        "category": selector.css(".label ::text").get(),
        }
    return results


# Requisito 5
def get_tech_news(amount):
    blog_url = "https://blog.betrybe.com/"
    page_html = fetch(blog_url)
    news_list = []
    last_news = []

    while len(news_list) < amount:
        news_list.extend(scrape_updates(page_html))
        blog_url = scrape_next_page_link(page_html)
        page_html = fetch(blog_url)

    for news in news_list[:amount]:
        html = fetch(news)
        html_text = scrape_news(html)
        last_news.append(html_text)

    create_news(last_news)

    return last_news
