from math import pi
from shape3d import Shape3D
from utils import validate_positive_number

class Sphere(Shape3D):
    def __init__(self, radius: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y, z)

        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        value = validate_positive_number(value)
        self._radius = value

    @property
    def circumference(self) -> float:
        return 2 * pi * self.radius

    @property
    def volume(self) -> float:
        return self.radius ** 3 * pi * 4 / 3

    @property
    def surface_area(self) -> float:
        return 4 * pi * self.radius**2

    def __str__(self):
        return f"A sphere with radius {self.radius} on position ({self.x}, {self.y}, {self.z})."

    def __repr__(self):
        return f"Sphere({self.radius}, {self.x}, {self.y}, {self.z})"