"""
This module initializes and configures the Flask application with SQLAlchemy, Marshmallow,
and Flask-Migrate. It also registers the application's blueprints for user and base routes.

Modules imported:
    - Flask: The core Flask application object.
    - Migrate: Flask-Migrate extension for SQLAlchemy database migrations.
    - SQLAlchemy: SQLAlchemy database extension for Flask.
    - Marshmallow: Marshmallow serialization/deserialization and validation library for Flask.
    - user_bp: Blueprint for user-related routes from `app.routes.user_route`.
    - base_bp: Blueprint for base routes from `app.routes.base_route`.

Functions:
    - create_app(config_filename=None): Initializes the Flask app with the given configuration
      file, sets up database migrations, initializes extensions, and registers blueprints.

Usage:
    To create an instance of the Flask application, call `create_app` with an optional
    configuration filename:
        app = create_app('path/to/config.py')
"""

from flask import Flask
from flask_injector import FlaskInjector
from flask_cors import CORS

from configuration import extensions
from configuration.services.services import Services
from configuration.config import DevelopmentConfig

app = Flask(__name__)
CORS(app)
# Load configuration
app.config.from_object(DevelopmentConfig)
extensions.init(app)

services = Services(app)
FlaskInjector(app=app, modules=[services.inject_services])


if __name__ == "__main__":
    app.run()
