from shape3d import Shape3D
from types import NotImplementedType
from utils import validate_positive_number, validate_number, validate_number_type

class Cube(Shape3D):
    def __init__(self, edge_length: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y, z)

        self.edge_length = edge_length

    @property
    def edge_length(self) -> float:
        return self._edge_length

    @edge_length.setter
    def edge_length(self, value: float) -> None:
        value = validate_positive_number(value)
        self._edge_length = value

    @property
    def surface_area(self) -> float:
        return 6 * (self.edge_length ** 2)

    @property
    def volume(self) -> float:
        return self.edge_length ** 3

    def __eq__(self, other) -> bool | NotImplementedType:
        """
        Compares the volume between two Shape3D objects of matching type. Returns False if the object types don't match.
        
        Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        if type(self) is not type(other):
            return False

        return self.volume == other.volume

    def __lt__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is less than another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume < other.volume

    def __gt__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is greater than another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume > other.volume

    def __ge__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is greater than or equal to another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume >= other.volume

    def __le__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is less than or equal to another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume <= other.volume        

    def __str__(self) -> str:
        return f"A cube with an edge length of {self.edge_length} on position ({self.x}, {self.y}, {self.z})."

    def __repr__(self) -> str:
        return f"Cube({self.edge_length}, {self.x}, {self.y}, {self.z})"