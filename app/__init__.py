from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# set secret key for session
app.secret_key = "asdfasoji10147"

from app import routes, models
from app import my_code  # my functions
