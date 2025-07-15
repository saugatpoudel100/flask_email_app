import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Load sender info from environment variables
SENDERS = {
    "gmail1": {
        "email": os.getenv("GMAIL1_EMAIL"),
        "password": os.getenv("GMAIL1_PASSWORD")
    },
    "gmail2": {
        "email": os.getenv("GMAIL2_EMAIL"),
        "password": os.getenv("GMAIL2_PASSWORD")
    },
}

LOG_FILE = "mail_log.txt"

def log_to_file(message):
    """
    Append a message to the log file using UTF-8 encoding
    to avoid UnicodeEncodeError with emojis.
    """
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def send_email(subject, html_body, recipients, sender_key, attachments=[]):
    """
    Send an email with HTML content and optional file attachments.
    Logs success or failure messages with timestamps.
    """
    sender = SENDERS.get(sender_key)
    if not sender:
        raise ValueError("Invalid sender key")

    msg = MIMEMultipart()
    msg["From"] = sender["email"]
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject

    # Attach the HTML message body
    msg.attach(MIMEText(html_body, "html"))

    # Attach files, if any
    for attachment in attachments:
        file_data = attachment.read()
        part = MIMEApplication(file_data, Name=attachment.filename)
        part["Content-Disposition"] = f'attachment; filename="{attachment.filename}"'
        msg.attach(part)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender["email"], sender["password"])
            server.sendmail(sender["email"], recipients, msg.as_string())

        log_to_file(f"✅ Email sent successfully from {sender['email']} to {recipients}")
        print("✅ Sent successfully")
        return True
    except Exception as e:
        log_to_file(f"❌ Failed to send email from {sender['email']} to {recipients}: {str(e)}")
        print("❌ Error sending:", e)
        return False
