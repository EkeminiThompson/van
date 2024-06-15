import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///vcf.db'  # Ensure this is a valid path for your SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
