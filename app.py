from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from flask_migrate import Migrate
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Migrate(app, db)

app.register_blueprint(auth)
