import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'changeme')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'sqlite:///messages.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
