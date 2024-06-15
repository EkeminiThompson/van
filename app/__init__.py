from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, instance_path='/tmp')

# Update your configuration settings here, if needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'  # Adjust this to your database URI

db = SQLAlchemy(app)

from app import routes, models  # Ensure this import is at the end
