from shape3d import Shape3D
from utils import validate_positive_number

class Cube(Shape3D):
    """
    Subclass of Shape3D for creating cubes.
    """
    def __init__(self, edge_length: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        """
        Initializes edge length as an attribute.

        x, y and z coordinates are initialized by the Shape3D superclass.
        """
        super().__init__(x, y, z)

        self.edge_length = edge_length

    @property
    def edge_length(self) -> float:
        """
        Returns the current edge length of a Cube object.
        """
        return self._edge_length

    @edge_length.setter
    def edge_length(self, value: float) -> None:
        """
        Validates the type of 'value' and stores it in an instance attribute.
        """
        value = validate_positive_number(value)
        self._edge_length = value

    @property
    def surface_area(self) -> float:
        """
        Calculates the surface area of a Cube object and returns it as a float.
        """
        return 6 * (self.edge_length ** 2)

    @property
    def volume(self) -> float:
        """
        Calculates the volume of a Cube object and returns it as a float.
        """
        return self.edge_length ** 3    

    def __str__(self) -> str:
        """
        Returns a human-readable description of a Cube object as a string.
        """
        return f"A cube with an edge length of {self.edge_length} on position ({self.x}, {self.y}, {self.z})."

    def __repr__(self) -> str:
        """
        Returns a string representation of a Cube object.
        """
        return f"Cube({self.edge_length}, {self.x}, {self.y}, {self.z})"