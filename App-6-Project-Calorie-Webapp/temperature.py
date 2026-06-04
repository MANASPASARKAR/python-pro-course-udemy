from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class Temperature:

    def __init__(self, city, country):
        self.city = city.replace(" ", "-")
        self.country = country.replace(" ", "-")

    def get(self):
        url = f"https://wttr.in/{self.city}+{self.country}"
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True
            )
            page = browser.new_page()
            page.goto(url)

            html = page.content()
            soup = BeautifulSoup(html, "html.parser")
            temp = soup.find("span", attrs={"class": "term-fgx220"})
            browser.close()
            if temp:
                return temp.text
            else:
                return -45
