# app/__init__.py

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_path='/tmp')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)
    return app
from app import routes, models  # Ensure this import is at the end
