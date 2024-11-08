from common.mail_client import MailClient

mail_client = MailClient(is_send=True)

was_send = mail_client.send_email("Test email", "This is a test email", ["dennisnguyen3000@yahoo.dk"])
print(f"was sent: {was_send}")