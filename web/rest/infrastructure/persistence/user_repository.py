from typing import Optional
from werkzeug.security import generate_password_hash

from configuration.extensions.db_extension import db
from domain.model.user.user import User
from domain.model.user.user_repository_interface import UserRepositoryInterface
from domain.utils.exceptions.domain_exception import DomainException
from infrastructure.persistence.sql_alchemy.user.user_mapped import UserMapped


class UserRepository(UserRepositoryInterface):
    """
    Repository class for managing user data persistence using SQLAlchemy.

    This class implements the UserRepositoryInterface and provides methods
    to add new users and retrieve users by their username from the database.
    """

    def __init__(self) -> None:
        self.db = db
        super().__init__()

    def add(self, **kwargs) -> User:
        user: UserMapped = UserMapped(
            username=kwargs.get("username"),
            password_hash=generate_password_hash(kwargs.get("password")),
        )
        self.db.session.add(user)
        self.db.session.commit()

        last_updated = (
            self.db.session.query(UserMapped).order_by(UserMapped.id.desc()).first()
        )

        if last_updated is None:
            return None

        return User(
            id=last_updated.id,
            username=last_updated.username,
            password_hash=last_updated.password_hash,
        )

    def get_by_username(self, username: str) -> User:
        user: Optional[UserMapped] = UserMapped.query.filter_by(
            username=username
        ).first()

        if user is None:
            raise DomainException("User not found")

        user_attrs = user.to_dict()
        return User(**user_attrs)
