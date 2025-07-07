from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5002)

# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Création des tables si nécessaire
    with app.app_context():
        db.create_all()

    # Enregistrement des routes
    from app.routes import register_routes
    register_routes(app)

    return app
