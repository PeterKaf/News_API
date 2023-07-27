import smtplib
import ssl
import os


def send_email(content):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("MAIL_APK_SENDER")
    sender_app_password = os.getenv("MAIL_APK_PASSWD")
    receiver_email = os.getenv("MAIL_APK_RECEIVER")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, receiver_email, content)
