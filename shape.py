from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

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