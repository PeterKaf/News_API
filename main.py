import requests
import datetime
import send_email
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


# SETUP
USE_ENV = True  # Set this to False if you want to use your own values instead of environment variables

# This script is set up to work with environment variables, you can use it as explained in the README.md file,
# or you can replace the variables with your own values, in a code block like the one commented below.

if USE_ENV:
    # Load environment variables from an .env file
    load_dotenv()  # Use this if the .env file is in the same directory as this script

    # Or, specify the path to a specific .env file via code like this:
    """
    dotenv_path = "/path/to/your/.env"
    # load_dotenv(dotenv_path)
    """
    # Assign environment variables to Python variables
    key = os.environ.get("NEWS_API_KEY")
    sender_email = os.environ.get("MAIL_APK_SENDER")
    sender_app_password = os.environ.get("MAIL_APK_PASSWD")
    receiver_email = os.environ.get("MAIL_APK_RECEIVER")
else:
    # In case you don`t want to use .env, you can replace the variables below with your own values
    # Be careful not to commit your API key or your email credentials to a public repository
    key = "ENTER YOUR OWN NEWS API KEY HERE"
    sender_email = "ENTER YOUR OWN EMAIL ADDRESS HERE"
    sender_app_password = "ENTER YOUR OWN APP PASSWORD HERE"
    receiver_email = "ENTER RECEIVER EMAIL ADDRESS HERE"


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
