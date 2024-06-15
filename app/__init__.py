# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(app.instance_path + '/your_database.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    db.init_app(app)

    with app.app_context():
        # Importing inside the function to avoid circular imports
        from . import routes, models

    return app
