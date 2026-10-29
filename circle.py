from shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius: float, x: float = 0, y: float = 0):
        super().__init__(x, y)

        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        if not isinstance(value, float | int) or isinstance(value, bool): # Safeguard against booleans as they are considered a subclass of int
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        self._radius = value

    @property
    def area(self):
        return pi * (self.radius**2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    def __repr__(self):
        return f"Circle({self.radius})"