from shape import Shape
from math import pi

class Circle(Shape):
    """
    Subclass of Shape for creating circles.
    """
    def __init__(self, radius: float, x: float = 0, y: float = 0) -> None:
        """
        Initializes radius as an attribute.

        x and y coordinates are initialized by the Shape superclass.
        """
        super().__init__(x, y)

        self.radius = radius

    @property
    def radius(self) -> float:
        """
        Returns the radius of a Circle object.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
        Validates the type of 'value' and stores it in an instance attribute.

        Invalid types raise TypeError. Negative or zero-values raise ValueError.
        """
        if not isinstance(value, float | int) or isinstance(value, bool): # Safeguard against booleans as they are considered a subclass of int
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        self._radius = value

    def is_unit_circle(self) -> bool:
        """
        Checks whether a Circle object is a unit circle.
        """
        return self.radius == 1

    @property
    def area(self) -> float:
        """
        Calculates the area of a Circle object and returns it as a float.
        """
        return pi * (self.radius**2)

    @property
    def perimeter(self) -> float:
        """
        Calculates the perimeter of a Circle object and returns it as a float.
        """
        return 2 * pi * self.radius

    def __str__(self) -> str:
        """
        Returns a human-readable description of a Circle object as a string.
        """
        return f"A circle with the radius {self.radius} on position ({self.x}, {self.y})"

    def __repr__(self) -> str:
        """
        Returns a Circle object and its values as a string.
        """
        return f"Circle({self.radius}, {self.x}, {self.y})"