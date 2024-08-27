"""
This module contains configuration classes for a Flask application.

Classes:
    Config: Base configuration class.
    DevelopmentConfig: Configuration class for development environment.
    ProductionConfig: Configuration class for production environment.
"""

import os


class Config:
    # pylint: disable=too-few-public-methods
    """
    Base configuration class.
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    ROOT_PATH = "/opt/stockflow"


class DevelopmentConfig(Config):
    # pylint: disable=too-few-public-methods
    """
    Development configuration class.

    Attributes:
        DEBUG (bool): Flag to enable debug mode in Flask for development purposes.
    """

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    # pylint: disable=too-few-public-methods

    """
    Production configuration class.

    Attributes:
        DEBUG (bool): Flag to disable debug mode in Flask for production purposes.
    """

    DEBUG = False
