import pandas as pd
import yagmail
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user="impasarkarmanas02@gmail.com", password="pfobnaaqluawnqna")
    email.send(to=f"{row['email']}",
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}, See whats on about {row['interest']} today.\n {news_feed.get()}\nManas")


while True:
    if datetime.datetime.now().hour == 18 and datetime.datetime.now().minute == 8:
        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()
            
    time.sleep(60)