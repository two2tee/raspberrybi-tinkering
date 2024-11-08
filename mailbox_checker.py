from gpiozero import DistanceSensor
from time import sleep
from datetime import datetime, timedelta
from hardware.lcd_display import LCD_Display
from common.mail_client import MailClient

lcd = LCD_Display(is_backlight=True, is_disabled=True)

check_frequency_sec_office_hours = 1.5
check_frequency_sec_off_hours = 30
dist_threshold = 0.5

last_sent_date  = None
email_is_send = True
email_send_timedelta_minutes = 60
mail_client = MailClient(is_send=email_is_send)

ultrasonic = DistanceSensor(echo=19, trigger=26, threshold_distance=dist_threshold)


def send_email():
    global last_sent_date
    current_time = datetime.now()

    if last_sent_date is not None and current_time - last_sent_date < timedelta(minutes=email_send_timedelta_minutes):
        print("email send limited.")
        return

    if not email_is_send:
        lcd.printMessageWithDelay(duration_sec=5, message='Email Disabled. Nothing sent', headerText="EmailStatus:")
        return

    body = """\
    You have received post in your mail box.
    -- This email was sent from raspberry pi."""

    subject = "New post in mailbox!"

    was_sent = mail_client.send_email(subject, body, ["dennisnguyen3000@yahoo.dk"])

    if was_sent:
        lcd.printMessageWithDelay(duration_sec=5, message='Email sent!', headerText="EmailStatus:")
        last_sent_date = datetime.now()


def try_sleep_until_next_check():
    current_time = datetime.now()
    if current_time.hour >= 6 and current_time.hour < 19:
        sleep(check_frequency_sec_office_hours)
    else:
        sleep(check_frequency_sec_off_hours)


## MAIN

lcd.printMessageWithDelay(duration_sec=3, message="V1.0.0", headerText="Mailbox checker")
lcd.printMessageWithDelay(duration_sec=3, message=f'{email_is_send}', headerText="EmailStatus:")


while True:
    try_sleep_until_next_check()
    dist = ultrasonic.distance
    lcd.printMessage(f'{dist}', headerText="Distance:")
    if(dist <= dist_threshold):
        send_email()
