import os
import time
import smtplib
import psutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')
from_address = os.getenv('FROM_ADDRESS')
to_address = os.getenv('TO_ADDRESS')

def send_email(smtp_server, smtp_port, smtp_username, smtp_password, from_address, to_address, subject, message):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()

def calculate_duration(start_time, end_time):
    duration = end_time - start_time
    minutes = int(duration / 60)
    seconds = int(duration % 60)
    return f"{minutes} minutes {seconds} seconds"

def main():
    last_power_plugged = None
    loadshed_start_time = None

    while True:
        battery = psutil.sensors_battery()
        power_plugged = battery.power_plugged

        if power_plugged != last_power_plugged:
            last_power_plugged = power_plugged
            if power_plugged:
                if loadshed_start_time is not None:
                    loadshed_end_time = time.time()
                    duration = calculate_duration(loadshed_start_time, loadshed_end_time)
                    message = f"Power status changed: AC plugged in\nLoadshed duration: {duration}"
                    send_email(smtp_server, smtp_port, smtp_username, smtp_password, from_address, to_address, "Loadshed Notification", message)
                    loadshed_start_time = None
            else:
                if loadshed_start_time is None:
                    loadshed_start_time = time.time()
                    message = "Power status changed: Running on battery"
                    send_email(smtp_server, smtp_port, smtp_username, smtp_password, from_address, to_address, "Loadshed Notification", message)

        time.sleep(60)

if __name__ == "__main__":
    main()