from app import twilio_client, Config

def send_otp(mobile, otp):
    twilio_client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=Config.TWILIO_PHONE_NUMBER,
        to=mobile
    )
