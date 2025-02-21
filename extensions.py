from flask_pymongo import PyMongo
from flask_mail import Mail
from twilio.rest import Client

mongo = PyMongo()
mail = Mail()
twilio_client = None  # Will be initialized in app factory
