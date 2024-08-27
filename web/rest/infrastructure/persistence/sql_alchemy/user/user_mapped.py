from dataclasses import dataclass

from sqlalchemy import inspect
from configuration.extensions.db_extension import db


@dataclass
class UserMapped(db.Model):
    """
    Represents a user in the database, mapped to the 'users' table.

    Attributes:
        id (int): The primary key of the user.
        username (str): The unique username of the user.
        password_hash (str): The hashed password of the user.

    Methods:
        get_model_attributes() -> dict:
            Retrieves a dictionary of the model's attributes and their current values.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(1024))

    def to_dict(self):
        mapper = inspect(self)
        attributes = {}
        for column in mapper.attrs:
            attributes[column.key] = getattr(self, column.key)
        return attributes
