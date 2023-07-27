import smtplib
import ssl
import os


def send_email(content):
    """
    Send email with news from NewsAPI.org
    :param content: String to be sent
    :return: None
    """
    port = 465
    smtp_server = "smtp.gmail.com"
    # Replace with your own credentials
    sender_email = os.getenv("MAIL_APK_SENDER")             # Enter your own address
    sender_app_password = os.getenv("MAIL_APK_PASSWD")      # Enter your app own password
    receiver_email = os.getenv("MAIL_APK_RECEIVER")         # Enter receiver own address

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, receiver_email, content)
