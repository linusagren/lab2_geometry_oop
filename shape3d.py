from abc import abstractmethod
from shape import Shape
from types import NotImplementedType
from utils import validate_number_type

class Shape3D(Shape):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y)

        z = validate_number_type(z)

        self._z = z

    @property
    def z(self) -> float:
        return self._z

    @property
    @abstractmethod
    def surface_area(self) -> float:
        ...

    @property
    @abstractmethod
    def volume(self) -> float:
        ...

    def translate(self, dx: float, dy: float, dz: float = 0) -> None:
        dz = validate_number_type(dz)
        
        super().translate(dx, dy)
        self._z = self.z + dz

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