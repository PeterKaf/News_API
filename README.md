# Project: Email News App

This project is an application that sends an email with the most recent news about a specified topic. It utilizes the NewsAPI to retrieve relevant news articles and uses the smtplib library to send the email.

## Project Structure

The project consists of two files:

1. `main.py`: This file contains the main function that retrieves the news articles and sends the email.
2. `send_email.py`: This file includes a helper function that sends the email.

## Getting Started

To run the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your email credentials and API key:

    <b>Do not share your credentials with others </b>
    - Replace `your_sender_email` with your own email address.
    - Replace `your_sender_app_password` with an app password generated for your email account.
    - Replace `your_receiver_email` with the email address where you want to receive the news.
    - Replace `your_news_api_key` with your NewsAPI API key.
   
4. Run the `main.py` file: `python main.py`.
5. Enter the topic you want to read about when prompted.

## Dependencies

The project requires the following dependencies. You can install them using the provided `requirements.txt` file:

- `requests`: For making HTTP requests to the NewsAPI.
- `bs4` (BeautifulSoup): For parsing the HTML description of the news articles.
- `smtplib`: For sending the email.
- `ssl`: For creating an SSL context.
