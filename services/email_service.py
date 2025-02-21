from flask import current_app

def send_verification_email(user_email):
    mail = current_app.extensions['mail']  # Get mail instance from Flask app context
    msg = mail.send_message(
        subject="Verify Your Email",
        recipients=[user_email],
        body="Your verification code is 12345"
    )
    return msg
