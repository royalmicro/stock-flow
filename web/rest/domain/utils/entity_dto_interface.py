from typing import Any, Dict, Protocol, Self


class EntityDtoInterface(Protocol):
    """
    Interface for converting an entity to a dictionary representation.

    Methods
    -------
    to_string() -> Dict[str, Any]:
        Converts the entity to a dictionary representation.
    """

    def to_dict(self) -> Dict[str, Any]: ...

    def from_dict(self, data: dict) -> Self: ...
