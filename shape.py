from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x: float = 0, y: float = 0):
        if not isinstance(x, float | int) or isinstance(x, bool):
            raise TypeError(f"'x' must be int or float, not {type(x).__name__}.")

        if not isinstance(y, float | int) or isinstance(y, bool):
            raise TypeError(f"'y' must be int or float, not {type(y).__name__}.")

        self._x = x
        self._y = y

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented

        if type(self) is not type(other):
            return False

        return self.area == other.area


    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

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
        self._x = self.x + dx
        self._y = self.y + dy