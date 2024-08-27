from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


class Migration:
    """
    A singleton class that initializes and manages database migrations for a Flask application.

    This class ensures that only one instance of Migration exists and provides methods to initialize
    the migration setup for a given Flask app using Flask-Migrate.

    Methods:
        __new__(cls, *args, **kwargs):
            Ensures a single instance of the Migration class is created.

        __init__(self):
            Initializes the Migrate instance for database migrations.

        init_migration(self, app: Flask, db: SQLAlchemy) -> None:
            Configures the Flask application for database migrations.

            Parameters:
                app (Flask): The Flask application instance to be configured for migrations.
                db (SQLAlchemy): The SQLAlchemy database instance to be configured for migrations.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Migration, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.migration_instance = Migrate()

    def init_migration(
        self, app: Flask, db: SQLAlchemy
    ) -> None:  # Prevent reinitialization
        self.migration_instance.init_app(app, db)
