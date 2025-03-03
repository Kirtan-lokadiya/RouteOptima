# routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from pymongo import MongoClient
import random, string, bcrypt
import pyrebase

from services.email_service import send_email_otp
from services.sms_service import send_sms
from services.hashing import hash_password

auth_bp = Blueprint('auth', __name__)

def get_firebase():
    """ Correctly initialize Firebase at runtime inside a request context """
    firebase = pyrebase.initialize_app(current_app.config['FIREBASE_CONFIG'])
    return firebase.auth()

def get_db():
    """ Get MongoDB connection """
    client = MongoClient(current_app.config["MONGO_URI"])
    db = client.get_default_database()  # Assumes the DB name is in the URI
    return db

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        current_app.logger.info("Signup form submitted")
        first_name = request.form.get('first_name')
        last_name  = request.form.get('last_name')
        email      = request.form.get('email')
        mobile     = request.form.get('mobile')
        password   = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Basic validation.
        if not all([first_name, last_name, email, mobile, password, confirm_password]):
            flash("All fields are required", "danger")
            return redirect(url_for('auth.signup'))
        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for('auth.signup'))
        if len(password) < 8:
            flash("Password must be at least 8 characters", "danger")
            return redirect(url_for('auth.signup'))

        db = get_db()
        if db.users.find_one({"email": email}):
            flash("Email already registered", "danger")
            return redirect(url_for('auth.signup'))

        # Hash password.
        hashed_password = hash_password(password)

        # Create user record.
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "mobile": mobile,
            "password": hashed_password,
            "email_verified": False,
            "mobile_verified": False
        }
        db.users.insert_one(user_data)
        current_app.logger.info("User inserted into database: %s", email)

        # Generate and send OTP for email verification.
        email_otp = ''.join(random.choices(string.digits, k=6))
        session['email_otp'] = email_otp
        session['user_email'] = email  # To know which user to update
        send_email_otp(email, first_name, email_otp)
        current_app.logger.info("Email OTP sent to: %s", email)

        # Generate and send OTP for mobile verification.
        mobile_otp = ''.join(random.choices(string.digits, k=6))
        session['mobile_otp'] = mobile_otp
        session['mobile'] = mobile
        send_sms(mobile, f"Your SwiftRoute OTP is {mobile_otp}")
        current_app.logger.info("OTP sent to mobile: %s", mobile)

        flash("Signup successful! Please verify your email and mobile.", "success")
        return redirect(url_for('auth.verify_email_otp'))
    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        db = get_db()
        user = db.users.find_one({"email": email})
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
                session['verified'] = True
                session['user_email'] = email
                flash("Logged in successfully!", "success")
                current_app.logger.info("User logged in: %s", email)
                return redirect(url_for('optimization.home'))
            else:
                flash("Invalid password.", "danger")
        else:
            flash("User not found.", "danger")
        return redirect(url_for('auth.login'))
    return render_template('login.html')

### ✅ Fixed Google Sign-In via Firebase
@auth_bp.route('/login/google')
def login_google():
    """ Redirect user to Google authentication page """
    redirect_uri = "http://127.0.0.1:5000/auth/callback"
    return redirect("https://accounts.google.com/o/oauth2/auth"
                    "?client_id=" + current_app.config['GOOGLE_CLIENT_ID'] +
                    "&redirect_uri=" + redirect_uri +
                    "&scope=email profile openid"
                    "&response_type=code")

@auth_bp.route('/auth/callback')
def auth_callback():
    """ Handle Google OAuth callback and authenticate the user via Firebase """
    code = request.args.get('code')
    if not code:
        flash("Google sign-in failed. Try again.", "danger")
        return redirect(url_for('auth.login'))

    try:
        firebase_auth = get_firebase()

        # Exchange authorization code for access token
        token = firebase_auth.sign_in_with_custom_token(code)
        user_info = firebase_auth.get_account_info(token['idToken'])['users'][0]

        # Store user session
        session['user_email'] = user_info['email']
        session['user_name'] = user_info.get('displayName', 'User')
        session['verified'] = True

        flash("Google Sign-In Successful!", "success")
        return redirect(url_for('optimization.home'))  # Redirect after login

    except Exception as e:
        current_app.logger.error(f"Google authentication failed: {e}")
        flash("Authentication error. Please try again.", "danger")
        return redirect(url_for('auth.login'))

@auth_bp.route('/logout')
def logout():
    """ Clear session and log user out """
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('auth.login'))
