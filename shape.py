from abc import ABC
from utils import validate_number_type

class Shape(ABC):
    """
    Abstract superclass for shared properties and methods of subclasses.
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Validates the types for x, y and initializes them as attributes.
        """
        x = validate_number_type(x)
        y = validate_number_type(y)

        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        """
        Get the current x-coordinate.
        """
        return self._x

    @property
    def y(self) -> float:
        """
        Get the current y-coordinate.
        """
        return self._y

    def translate(self, dx: float, dy: float) -> None:
        """
        Moves a shape based on its current position.
        """
        dx = validate_number_type(dx)
        dy = validate_number_type(dy)
                
        self._x = self.x + dx
        self._y = self.y + dy