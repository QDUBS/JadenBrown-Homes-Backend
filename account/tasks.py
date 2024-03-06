from celery import shared_task

from account.models import Account
from lib.generate_token import generate_token
from lib.mail import Email
from mails.password_reset import reset_password_html

@shared_task
def send_reset_password_email(email, token):
    email_sender = Email()
    html = reset_password_html(token)
    subject = "Password Reset | MarksFildes"
    from_address = "benwebdev29@gmail.com"
    email_sender.set_heading(from_address=from_address, to_address=email, subject=subject)
    email_sender.html_email(html)
    return "Email sent"