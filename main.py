import requests
import datetime
import send_email
import os

date = datetime.date.today()
date = date - datetime.timedelta(days=1)
print(date)

topic = "Poland"
url = f"https://newsapi.org/v2/everything?q={topic}&apiKey=46eb96df333448d28f904668d1642d92&" \
      f"from={date}&sortBy=relevancy&language=en&pageSize=5"
key = os.getenv("NEWS_API_KEY")

requests = requests.get(url)
data = requests.json()
content = """\
Subject: News from NewsAPI.org\n
"""
for article in data["articles"]:
    title = article["title"]
    description = article["description"]
    news_url = article["url"]
    content += f"Title: {title}\nDescription: {description}\nURL: {news_url}\n\n"

send_email.send_email(content.encode("utf-8"))
