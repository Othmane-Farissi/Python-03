from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class for characters."""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the alive state of the character."""
        pass


class Stark(Character):
    """Stark family member."""

    def die(self):
        """Mark this Stark as dead."""
        self.is_alive = False
