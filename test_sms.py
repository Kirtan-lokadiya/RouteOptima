from twilio.rest import Client

# Replace these with your actual Twilio credentials from your Twilio Console
account_sid = 'AC9d38cc0ae337d55b13ab70e84d9891f6'
auth_token = '8924e50ac41dc0117255b7f286b0ec02'
twilio_phone_number = '+16824246736'
recipient_number = '+919328823998'  # Replace with your test phone number

client = Client(account_sid, auth_token)

# Generate a test OTP (in your actual application, this would be generated dynamically)
test_otp = '123456'

message = client.messages.create(
    body=f"Your test OTP is {test_otp}",
    from_=twilio_phone_number,
    to=recipient_number
)

print("Message SID:", message.sid)
