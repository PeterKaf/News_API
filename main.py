import requests
import datetime
import send_email
import os
from bs4 import BeautifulSoup


# SETUP
# This script is set up to work with environment variables, you can use it as explained in the README.md file,
# or you can replace the variables with your own values, in a code block like the one commented below.

# Set up your own credentials in environment variables (See README.md for more info)
key = os.getenv("NEWS_API_KEY")
sender_email = os.getenv("MAIL_APK_SENDER")
sender_app_password = os.getenv("MAIL_APK_PASSWD")
receiver_email = os.getenv("MAIL_APK_RECEIVER")

# Or just replace the variables with your own values, like this:
"""
key = "ENTER YOUR OWN NEWS API KEY HERE
sender_email = "ENTER YOUR OWN EMAIL ADDRESS HERE"
sender_app_password = "ENTER YOUR OWN APP PASSWORD HERE"
receiver_email = "ENTER RECEIVER EMAIL ADDRESS HERE"
"""


date = datetime.date.today()
date = date - datetime.timedelta(days=1)

topic = input("What topic do you want to read about? ")

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

send_email.send_email(content.encode("utf-8"), sender_email, sender_app_password, receiver_email)
