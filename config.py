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
    TWILIO_PHONE_NUMBER = '+16824246736'

    # Google OAuth configuration
    GOOGLE_CLIENT_ID = '21115487922-a0kapdku67mea9d5jjmvanij65gqapdk.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
    GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    GOOGLE_REDIRECT_URI = 'http://127.0.0.1:5000/login/callback'  # Add this line

    # Firebase Configuration
    FIREBASE_CONFIG = {
        "apiKey": "AIzaSyBe1usSRP28OEDRcpzYzm5zg4jqQG6Dhi4",
        "authDomain": "sgp-auth-88668.firebaseapp.com",
        "projectId": "sgp-auth-88668",
        "storageBucket": "sgp-auth-88668.firebasestorage.app",
        "messagingSenderId": "930661295427",
        "databaseURL": "https://sgp-auth-88668-default-rtdb.firebaseio.com/",
        "appId": "1:930661295427:web:173b0a68211676cb24bbf6",
        "measurementId": "G-EZJKTXEZ7K"
    }
