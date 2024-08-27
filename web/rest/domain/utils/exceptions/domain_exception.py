class DomainException(Exception):
    """Base exception for domain-related errors."""

    def __init__(self, message=None):
        if message is None:
            self.message = "An error occurred in the domain logic."
        super().__init__(message)
