# 📧 Flask Email Sender via Gmail SMTP

A secure Flask web app for sending emails using **multiple Gmail SMTP accounts** with features like:

- ✅ HTML email support  
- ✅ Multiple recipients  
- ✅ File attachments  
- ✅ Sender account selection  
- ✅ IP whitelist protection  
- ✅ `.env` configuration  
- ✅ UTF-8 encoded logging

---

## 🚀 Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/saugatpoudel100/flask-email-sender.git
cd flask-email-sender
```

## 🛠️ Setup Instructions
1. Create Virtual Environment
Run the following commands depending on your OS:

```bash
Copy code
python -m venv venv
Activate virtual environment:

On Mac/Linux:
```
bash
Copy code
source venv/bin/activate
On Windows:

powershell
Copy code
venv\Scripts\activate
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Configure .env
Create a .env file in the root directory with the following content:

env
Copy code
FLASK_SECRET_KEY=your_secret_key
ALLOWED_IPS=127.0.0.1

GMAIL1_EMAIL=yourgmail1@gmail.com
GMAIL1_PASSWORD=your_app_password1

GMAIL2_EMAIL=yourgmail2@gmail.com
GMAIL2_PASSWORD=your_app_password2
⚠️ Important:
You must enable 2-Step Verification on your Gmail accounts
and generate App Passwords to use instead of your Gmail password.

🔐 IP Whitelist Security
Only users from IPs listed in the ALLOWED_IPS variable (comma-separated) in the .env file can access the app.

▶️ Running the App
Start the Flask app with:

bash
Copy code
python app.py
Then open your browser and go to:
http://127.0.0.1:5000

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
Sample content of mail_log.txt:

vbnet
Copy code
2025-07-15 10:32:23 - ✅ Email sent successfully from yourgmail1@gmail.com to ['test@example.com']
2025-07-15 10:35:12 - ❌ Failed to send email from yourgmail2@gmail.com to ['xyz@abc.com']: SMTPAuthenticationError...
🧪 Testing Checklist
✅ Use real Gmail accounts with App Passwords

✅ Access only from allowed IPs (ALLOWED_IPS in .env)

✅ Check your inbox & spam folder

✅ Review mail_log.txt for logs

🧰 Tech Stack
Python 3.7+

Flask

Gmail SMTP (smtp.gmail.com)

MIME (for HTML and attachments)

python-dotenv for environment variable loading

📎 License
MIT License

👨‍💻 Author
Built by Saugat Poudel
Feel free to contribute, fork, or suggest improvements!