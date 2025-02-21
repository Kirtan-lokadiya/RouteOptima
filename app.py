from flask import Flask
from config import Config
from extensions import mongo, mail, twilio_client
from routes.auth import auth_bp
from routes.optimization import optimize_bp
from twilio.rest import Client

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    mongo.init_app(app)
    mail.init_app(app)
    global twilio_client
    twilio_client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(optimize_bp, url_prefix='/optimize')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
