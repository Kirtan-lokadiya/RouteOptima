class Config:
    SECRET_KEY = 'your_secret_key'
    MONGO_URI = "mongodb+srv://<user>:<password>@cluster.mongodb.net/<db>?retryWrites=true&w=majority"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_app_password'
    TWILIO_ACCOUNT_SID = "your_twilio_sid"
    TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
    TWILIO_PHONE_NUMBER = "+1234567890"
