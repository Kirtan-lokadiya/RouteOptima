from flask import Flask
from flask_pymongo import PyMongo
from flask_mail import Mail
from twilio.rest import Client
from config import Config
from routes.auth import auth_bp
from routes.optimization import optimize_bp

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
mongo = PyMongo(app)
mail = Mail(app)
twilio_client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(optimize_bp, url_prefix='/optimize')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
