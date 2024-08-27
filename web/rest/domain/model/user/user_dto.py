from domain.model.user.user_interface import UserInterface
from domain.utils.entity_dto_interface import EntityDtoInterface


class UserDto(EntityDtoInterface):
    """
    UserDto class representing a Data Transfer Object for the User entity.

    This class is used to transfer data between layers in a decoupled manner.
    """

    def __init__(self, user: UserInterface):
        self.id = user.get_id()
        self.username = user.get_username()

    def __repr__(self) -> str:
        return f"UserDto(id={self.id}, username='{self.username}')"

    def get_id(self) -> int:
        return self.id

    def get_username(self) -> str:
        return self.username
