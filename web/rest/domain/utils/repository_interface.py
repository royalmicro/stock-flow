from typing import Protocol

from domain.utils.entity_interface import EntityInterface


class RepositoryInterface(Protocol):
    """
    Interface for converting an entity to its corresponding DTO (Data Transfer Object).

    Methods
    -------
    entity_to_dto() -> EntityDtoInterface:
        Converts the entity to its corresponding Data Transfer Object (DTO).
    """

    def add(self, **kwargs) -> EntityInterface: ...
    def delete(self, entity_id: str | int) -> None: ...
    def update(self, entity: EntityInterface) -> EntityInterface: ...
