# filepath: /home/kirtan/Downloads/RouteOptima-main/test_email.py
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kirtanlokadiya998@gmail.com'
app.config['MAIL_PASSWORD'] = 'fxxh pqmo upzz osgg'

mail = Mail(app)

with app.app_context():
    msg = Message("Test Email", sender=app.config['MAIL_USERNAME'], recipients=["recipient@example.com"])
    msg.body = "This is a test email."
    try:
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")