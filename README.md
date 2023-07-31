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

   *There are two options to set up credentials:*

   **Option 1: Provide Credentials in `.env` File (Recommended)**

   - Create a `.env` file in the project directory.
   - Add the following lines to the `.env` file:

     ```
     MAIL_APK_SENDER=your_sender_email 
     MAIL_APK_PASSWD=your_sender_app_password 
     MAIL_APK_RECEIVER=your_receiver_email 
     NEWS_API_KEY=your_news_api_key
     ```
   - Replace the values with your own credentials.
   
   **Option 2: Change variables inside `main.py` file**

   - Open the `main.py` file.
   - Change from True to False the following line:
     ```
     USE_ENV = True
     ```
   - Locate the following variables inside:

     ```
     key = "ENTER YOUR OWN NEWS API KEY HERE
     sender_email = "ENTER YOUR OWN EMAIL ADDRESS HERE"
     sender_app_password = "ENTER YOUR OWN APP PASSWORD HERE"
     receiver_email = "ENTER RECEIVER EMAIL ADDRESS HERE"
     ```
   - Replace the values with your own credentials.
   - 

   <b>Note: Make sure to keep your credentials secure and do not share them with others.</b>
4. Run the `main.py` file: `python main.py`.
5. Enter the topic you want to read about when prompted.
6. Check your email inbox for the news articles.

## Dependencies

The project requires the following dependencies. You can install them using the provided `requirements.txt` file:

- `requests`: For making HTTP requests to the NewsAPI.
- `bs4` (BeautifulSoup): For parsing the HTML description of the news articles.
- `smtplib`: For sending the email.
- `ssl`: For creating an SSL context.
- `dotenv`: For loading environment variables from a `.env` file.
