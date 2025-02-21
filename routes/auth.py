# from flask import Blueprint, render_template, request, redirect, url_for, flash, session
# from services.email_service import send_verification_email
# from services.sms_service import send_otp
# from services.hashing import hash_password
# from extensions import mongo

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         data = request.form
#         hashed_pw = hash_password(data['password'])
#         mongo.db.users.insert_one({
#             "first_name": data['first_name'],
#             "last_name": data['last_name'],
#             "email": data['email'],
#             "password": hashed_pw,
#             "mobile": data['mobile'],
#             "is_verified": False
#         })
#         send_verification_email(data['email'])
#         flash("Signup complete! Verify your email.")
#         return redirect(url_for('auth.verify_email'))
#     return render_template('signup.html')
