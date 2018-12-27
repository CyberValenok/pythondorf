from flask import Flask
from flask_bcrypt import Bcrypt
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

from ums import models
from ums import urls
