class Config:
    SECRET_KEY = 'your-secret-key'
    MONGO_URI = 'mongodb+srv://harsheel:harsheel@auth.kfaj4.mongodb.net/test?retryWrites=true&w=majority&appName=auth'
    
    # Flask-Mail configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pawarharsh3378@gmail.com'
    MAIL_PASSWORD = 'jqyy zljq okeh nwhy'
    
    # Twilio configuration for SMS
    TWILIO_ACCOUNT_SID = 'AC9d38cc0ae337d55b13ab70e84d9891f6'
    TWILIO_AUTH_TOKEN = '8924e50ac41dc0117255b7f286b0ec02'
    TWILIO_PHONE_NUMBER = '+16824246736'