from django.db.models.signals import pre_save
from django.dispatch import receiver
from account.models import Account
from lib.generate_token import generate_token
from lib.mail import Email
from mails.email_verification import email_verification_html

email = Email()

@receiver(pre_save, sender=Account)
def account_signal_handler(sender, instance, *args, **kwargs):
    if not instance.is_oauth:
        try:
            subject = "Email Verification | MarksFildes"
            from_address = "benwebdev29@gmail.com"
            payload = {"email":instance.email}
            token = generate_token(payload)
            html = email_verification_html(token=token)
            email.set_heading(from_address=from_address, to_address=instance.email, subject=subject)
            email.html_email(html)
        except Exception as exec:
            print(exec)
