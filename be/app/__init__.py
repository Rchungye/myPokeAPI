from functools import wraps
import os
from flask import Flask, Blueprint
from app.config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_apispec import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)

enviroment = config["ambiente"]
app.config.from_object(enviroment)

# Configuración Swagger
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Pokemon API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})

db = SQLAlchemy(app)
docs = FlaskApiSpec(app)
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

