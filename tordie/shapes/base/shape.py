from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def __str__(self):
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        pass
