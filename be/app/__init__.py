from functools import wraps
import os
from flask import Flask
from app.config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")

app = Flask(__name__)

enviroment = config["ambiente"]
app.config.from_object(enviroment)
db = SQLAlchemy(app)

Migrate(app, db)
CORS(app, supports_credentials=True)

app.config["SECURITY_TRACKABLE"] = True
app.config["SECRET_KEY"] = os.getenv("SKEY")