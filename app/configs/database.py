from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)

    from app.models.models_leads import Leads
    
    app.db = db

    db.create_all(app=app)

