from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os
from utils.email_utils import send_email

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Allowed IPs for security (comma separated in .env)
ALLOWED_IPS = os.getenv("ALLOWED_IPS", "").split(",")

@app.before_request
def restrict_ip():
    # Deny access if request's IP is not in allowed list
    if request.remote_addr not in ALLOWED_IPS:
        return "403 Forbidden: Your IP is not allowed", 403

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sender = request.form.get("sender")
        recipients = request.form.get("recipients", "").replace(" ", "").split(",")
        subject = request.form.get("subject")
        html_body = request.form.get("html_body")
        attachments = request.files.getlist("attachments")

        success = send_email(subject, html_body, recipients, sender, attachments)
        return redirect("/")

    return render_template("send_email.html")

if __name__ == "__main__":
    app.run(debug=True)
