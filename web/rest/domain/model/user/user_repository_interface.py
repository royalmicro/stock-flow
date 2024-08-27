from domain.utils.entity_interface import EntityInterface
from domain.utils.repository_interface import RepositoryInterface
from domain.model.user.user import User


class UserRepositoryInterface(RepositoryInterface):
    """
    Interface for user repository operations.

    This interface defines the contract for user repository implementations,
    including methods to retrieve a user by username and to add a new user entity.
    """

    def __init__(self) -> None:
        pass

    def get_by_username(self, username: str) -> EntityInterface:
        pass

    def add_entity(self, user: User) -> EntityInterface:
        pass
