from functools import wraps
import os
from flask import Flask
from app.config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
enviroment = config["ambiente"]
app.config.from_object(enviroment)


db = SQLAlchemy(app)
Migrate(app, db)
CORS(app, supports_credentials=True)


from app.routes.AbilityRoute import *
from app.routes.MoveRoute import *
from app.routes.PkmRoute import *


@app.cli.command()
def seed():
        """Add seed data to the database."""
        from seed_inicial import seed_db
        seed_db()

