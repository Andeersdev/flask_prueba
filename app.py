from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.car import Car
from utils.db import db
from routes.car_route import cars


def create_app():
    # Create app
    app = Flask(__name__)

    # SQLAlchemy configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_crud'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Execute tables
    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(cars)
    return app
