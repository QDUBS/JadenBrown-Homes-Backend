import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

load_dotenv()
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")

class Email():
    def __init__(self):
        self.message = MIMEMultipart("alternative")
        self.to_address = ""
        self.from_address = ""
        self.subject = ""

    def __create_smtp_server(self):
        try:
            with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp_server:
                smtp_server.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
                smtp_server.sendmail(from_addr=self.from_address,
                             to_addrs=self.to_address, 
                             msg=self.message.as_string())

        except Exception as exec:
            print(exec)

    
    def set_heading(self, subject, from_address, to_address):
        self.from_address = from_address
        self.to_address = to_address
        if "subject" in self.message:
            del self.message["subject"]  # Remove existing "Subject" header
        self.message["subject"] = subject
        self.message["from"] = self.from_address

    def html_email(self,html):
        self.message.attach(MIMEText(html, "html"))
        self.__create_smtp_server()
        
    def plain_email(self, text):
        self.message.attach(MIMEText(text, "plain"))
        self.__create_smtp_server()
