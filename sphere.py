from math import pi
from shape3d import Shape3D
from utils import validate_positive_number

class Sphere(Shape3D):
    """
    Subclass of Shape3D for creating spheres.
    """
    def __init__(self, radius: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        """
        Initializes radius as an attribute.

        x, y and z coordinates are initialized by the Shape3D superclass.
        """
        super().__init__(x, y, z)

        self.radius = radius

    @property
    def radius(self) -> float:
        """
        Returns the current radius of a Sphere object.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
        Validates the type of 'value' and stores it in an instance attribute.
        """
        value = validate_positive_number(value)
        self._radius = value

    @property
    def circumference(self) -> float:
        """
        Calculates the circumference of a Sphere object and returns it as a float.
        """
        return 2 * pi * self.radius

    @property
    def volume(self) -> float:
        """
        Calculates the volume of a Sphere object and returns it as a float.
        """
        return self.radius ** 3 * pi * 4 / 3

    @property
    def surface_area(self) -> float:
        """
        Calculates the surface area of a Sphere object and returns it as a float.
        """
        return 4 * pi * self.radius**2

    def __str__(self) -> str:
        """
        Returns a human-readable description of a Sphere object as a string.
        """
        return f"A sphere with radius {self.radius} on position ({self.x}, {self.y}, {self.z})."

    def __repr__(self) -> str:
        """
        Returns a string representation of a Sphere object.
        """
        return f"Sphere({self.radius}, {self.x}, {self.y}, {self.z})"