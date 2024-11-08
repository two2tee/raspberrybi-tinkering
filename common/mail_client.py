import json
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailClient:
    def __init__(self, is_send=True, config_path=""):
        self.is_send = is_send

        config_path = "mail_config.json" if config_path is "" else config_path
        config_file = open(config_path, "rt")
        if len(config_file) is 0:
            raise Exception("config file missing")

        self.config = json.loads(config_file)


    def send_email(self, subject: str, body: str, to_emails:[]) -> bool:
        if not self.is_send:
            print("email disabled.")
            return True

        email_smtp_host = self.config["smtpHost"]
        email_port = self.config["port"]
        from_email =  self.config["sender"] if from_email is "" else from_email
        to_emails = self.config["recipients"] if to_emails is [] else to_emails

        message = MIMEMultipart()
        message['From'] = from_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(email_smtp_host, email_port, context=context) as server:
            server.login(from_email, self.config["password"])
            server.sendmail(from_email, to_emails, message.as_string())
            print("email sent.")

        return True
