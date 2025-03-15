from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemondb.sqlite'
app.secret_key = b'huhjuytdf678ijo;k8uy'
# app.config['SECRET_KEY'] = b'huhjuytdf678ijo;k8uy'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from pokedex import models, routes