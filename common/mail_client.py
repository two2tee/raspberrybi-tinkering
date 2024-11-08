import json
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailClient:
    def __init__(self, is_send=True, config_path=""):
        self.is_send = is_send

        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, "mail_config.json") if config_path == "" else config_path
        print(config_path)

        with open(config_path, "rt") as config_file:
            config_content = config_file.read()
            if len(config_content) == 0:
                raise Exception("config file missing")

            self.config = json.loads(config_content)

    def send_email(self, subject: str, body: str, to_emails) -> bool:
        if not self.is_send:
            print("email disabled.")
            return True

        email_smtp_host = self.config["smtpHost"]
        email_port = self.config["port"]
        from_email =  self.config["sender"]
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
