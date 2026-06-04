# news api - 564a93f710114da1a6dc01e3d64818c8
# url - https://newsapi.org/v2/everything?q=tesla&from=2026-05-04&sortBy=publishedAt&apiKey=564a93f710114da1a6dc01e3d64818c8
from typing import Any

import requests

class NewsFeed:
    """
    representing multiple used titles and links as a single string
    """

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "564a93f710114da1a6dc01e3d64818c8"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = self._build_url()

        articles = self._fetch_articles(url)

        email_body = " "

        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _fetch_articles(self, url: str) -> Any:
        res = requests.get(url)
        content = res.json()
        articles = content['articles']
        return articles

    def _build_url(self) -> str:
        url = (f"{self.base_url}"
               f"q={self.interest}&"
               f"from={self.from_date}&"
               f"to={self.to_date}&"
               f"language={self.language}&"
               f"apiKey={self.api_key}")
        return url

# newsfeed = NewsFeed(interest='no', from_date='2026-06-02', to_date='2026-06-06', language='en')
# print(newsfeed.get())


