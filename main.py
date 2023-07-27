import requests
import datetime
import send_email
import os
from bs4 import BeautifulSoup

date = datetime.date.today()
date = date - datetime.timedelta(days=1)

topic = input("What topic do you want to read about? ")
key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}" \
      f"&apiKey={key}" \
      f"&from={date}" \
      "&sortBy=relevancy" \
      "&language=en"


response = requests.get(url)
data = response.json()
content = """\
Subject: News from NewsAPI.org
Content-Type: text/html

"""

for article in data["articles"][:5]:
    title = article["title"]
    description = article["description"]
    news_url = article["url"]

    soup = BeautifulSoup(description, "html.parser")
    stripped_description = soup.get_text()

    content += f"<strong>Title:</strong> {title}<br><strong>Description:</strong> {stripped_description}" \
               f"<br><strong>URL:</strong> {news_url}<br><br>"

send_email.send_email(content.encode("utf-8"))
