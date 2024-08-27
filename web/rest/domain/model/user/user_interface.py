from domain.utils.entity_interface import EntityInterface


class UserInterface(EntityInterface):
    """
    Interface for user repository operations.

    This interface defines the contract for user repository implementations,
    including methods to retrieve a user by username and to add a new user entity.
    """

    def __init__(self) -> None:
        pass

    def get_username(self) -> str:
        pass

    def get_id(self) -> int | None:
        pass
