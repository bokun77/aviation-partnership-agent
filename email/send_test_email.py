import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv("email/.env")

sender = os.getenv("SMTP_USER")
password = os.getenv("SMTP_PASSWORD")
recipient = os.getenv("TEST_RECIPIENT")

msg = EmailMessage()

msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = "TEST - Aviation Partnership Agent"

msg.set_content("""
Hello Djordje,

This is the first test email sent by the Aviation Partnership Agent.

The email delivery workflow is working correctly.

Project:
Never Too Late To Fly — Dj.B. Aviation Impact Project

Sender:
aviationimpact.project@gmail.com

Best regards,
Aviation Partnership Agent
""")

print("Connecting to Gmail...")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    print("Logged in successfully")

    smtp.send_message(msg)

print("Test email sent successfully")