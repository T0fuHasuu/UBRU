from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off modification tracking

db = SQLAlchemy(app)

# Import models and routes after db initialization
from epl import models, routes
