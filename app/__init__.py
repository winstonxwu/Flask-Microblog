from flask import Flask # the class Flask from the module flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config) # configuring and applying the secret key
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app) #initializing the the login function for the app so the user can stay logged in
login.login_view = 'login'

from app import routes, models # avoids circular imports, which can happen with Flask. Routes module needs to import the app variable, so having the import at the bottom stops the two files from referencing themselves in a circle