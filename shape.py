from abc import ABC, abstractmethod
from types import NotImplementedType

class Shape(ABC):
    """
    Abstract superclass for shared properties and methods of subclasses.
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Validates the types for x, y and initializes them as attributes.
        """
        if not isinstance(x, float | int) or isinstance(x, bool):
            raise TypeError(f"'x' must be int or float, not {type(x).__name__}.")

        if not isinstance(y, float | int) or isinstance(y, bool):
            raise TypeError(f"'y' must be int or float, not {type(y).__name__}.")

        self._x = x
        self._y = y

    def __eq__(self, other) -> bool | NotImplementedType:
        """
        Compares the areas between two Shape objects of matching type. Returns False if the object types don't match.
        
        Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape):
            return NotImplemented

        if type(self) is not type(other):
            return False

        return self.area == other.area

    def __lt__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is less than another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape):
            return NotImplemented

        return self.area < other.area

    def __gt__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is greater than another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape):
            return NotImplemented

        return self.area > other.area

    def __ge__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is greater than or equal to another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape):
            return NotImplemented

        return self.area >= other.area

    def __le__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is less than or equal to another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape):
            return NotImplemented

        return self.area <= other.area

    @property
    @abstractmethod
    def area(self) -> float:
        """
        Adds area as a requirement for subclasses.
        """
        ...

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """
        Adds perimeter as a requirement for subclasses.
        """
        ...

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
        if not isinstance(dx, int | float) or isinstance(dx, bool):
            raise TypeError(f"'dx' must be int or float, not {type(dx).__name__}.")
        
        if not isinstance(dy, int | float) or isinstance(dy, bool):
            raise TypeError(f"'dy' must be int or float, not {type(dy).__name__}.")
        
        self._x = self.x + dx
        self._y = self.y + dy