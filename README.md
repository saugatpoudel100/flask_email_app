# 📧 Secure Flask Gmail SMTP Email Sender

A Flask-based web app to send emails using **multiple Gmail SMTP accounts** with:

✅ HTML content  
✅ Multiple recipients  
✅ File attachments  
✅ Sender account selection  
✅ IP whitelist protection  
✅ `.env`-based environment configuration  
✅ UTF-8 logging to `mail_log.txt`

---

## 🚀 Features

- Send emails using Gmail SMTP
- Choose from multiple Gmail accounts (e.g., `gmail1`, `gmail2`)
- Attach one or more files
- Send to multiple recipients (comma-separated)
- Protect access using IP whitelisting
- Uses environment variables via `.env` for credentials and config
- Logs success/failure with timestamps in `mail_log.txt`

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/saugatpoudel100/flask-email-sender.git
cd flask-email-sender
2. Create virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate         # For Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure .env
Create a .env file in the root directory:

env
Copy code
FLASK_SECRET_KEY=your_secret_key
ALLOWED_IPS=127.0.0.1

GMAIL1_EMAIL=yourgmail1@gmail.com
GMAIL1_PASSWORD=your_app_password1

GMAIL2_EMAIL=yourgmail2@gmail.com
GMAIL2_PASSWORD=your_app_password2
⚠️ Make sure to enable 2-Step Verification and create an App Password for Gmail.

🔐 IP Whitelist Security
Only requests from IPs listed in ALLOWED_IPS (comma-separated) will be allowed to access the app.

▶️ Running the App
bash
Copy code
python app.py
Visit: http://127.0.0.1:5000

📂 File Structure
bash
Copy code
.
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── send_email.html
├── utils/
│   └── email_utils.py
└── mail_log.txt         # auto-created when emails are sent
📤 Log Output Example
Logs are stored in mail_log.txt with timestamps:

vbnet
Copy code
2025-07-15 10:32:23 - ✅ Email sent successfully from yourgmail1@gmail.com to ['test@example.com']
2025-07-15 10:35:12 - ❌ Failed to send email from yourgmail2@gmail.com to ['xyz@abc.com']: SMTPAuthenticationError...
🧪 Testing
To test locally:

Use real Gmail accounts with App Passwords.

Access only from IPs listed in .env.

Check your inbox & spam folder.

View mail_log.txt for results.

🧰 Tech Stack
Python 3.7+

Flask

Gmail SMTP (smtp.gmail.com)

MIME for email formatting

dotenv for config management

📎 License
MIT License

👨‍💻 Author
Built by [ Saugat]
Feel free to contribute, fork, or suggest improvements!


