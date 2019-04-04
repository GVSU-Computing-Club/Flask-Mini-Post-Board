from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

my_app = Flask(__name__)
my_app.config.from_object(Config)
db = SQLAlchemy(my_app)

from app import routes, models



