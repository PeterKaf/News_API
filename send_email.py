import smtplib
import ssl


def send_email(content, sender_email, sender_app_password, receiver_email):
    """
    This function sends an email with content provided
    :param content: string with the content of the email
    :param sender_email: string with the email address of the sender
    :param sender_app_password: string with the app password of the sender
    :param receiver_email: string with the email address of the receiver
    :return: None
    """
    port = 465
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, receiver_email, content)
