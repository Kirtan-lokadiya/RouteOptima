import logging
from flask import Flask, session, redirect, url_for, request
from config import Config
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from authlib.integrations.flask_client import OAuth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set up Logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    app.logger.info("Application startup")

    # Initialize Extensions
    mail = Mail(app)
    bcrypt = Bcrypt(app)

    # Initialize OAuth
    oauth = OAuth(app)
    google = oauth.register(
        'google',
        client_id=app.config.get("GOOGLE_CLIENT_ID"),
        client_secret=app.config.get("GOOGLE_CLIENT_SECRET"),
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        client_kwargs={'scope': 'openid email profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile'},
        redirect_uri='http://127.0.0.1:5000/authorized'
    )

    # Register blueprints
    from routes.auth import auth_bp
    from routes.optimization import optimization_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(optimization_bp)

    # Add OAuth to app context
    app.oauth = oauth
    app.google = google

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('auth.login'))

    @app.route('/authorized')
    def authorized():
        token = oauth.google.authorize_access_token()
        user = oauth.google.parse_id_token(token)
        session['user'] = user
        return redirect('/')

    @app.route('/login')
    def login():
        redirect_uri = url_for('authorized', _external=True)
        return oauth.google.authorize_redirect(redirect_uri)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
