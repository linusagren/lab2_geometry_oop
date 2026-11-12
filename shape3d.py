from abc import abstractmethod
from shape import Shape
from types import NotImplementedType
from utils import validate_number_type

class Shape3D(Shape):
    """
    Abstract superclass for shared and required properties and methods of the Cube and Sphere subclasses.
    """
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        """
        Validates the types for x, y, z and initializes them as attributes.
        """
        super().__init__(x, y)

        z = validate_number_type(z)

        self._z = z

    @property
    def z(self) -> float:
        """
        Returns the current z-coordinate of a Shape3D object.
        """
        return self._z

    @property
    @abstractmethod
    def surface_area(self) -> float:
        """
        Required method for subclasses to calculate surface area.
        """
        ...

    @property
    @abstractmethod
    def volume(self) -> float:
        """
        Required method for subclasses to calculate volume.
        """
        ...

    def translate(self, dx: float, dy: float, dz: float = 0) -> None:
        """
        Validates and moves a Shape3D based on its current position.
        """
        dz = validate_number_type(dz)
        
        super().translate(dx, dy)
        self._z = self.z + dz

    def __eq__(self, other: Shape) -> bool | NotImplementedType:
        """
        Compares the volume between two Shape3D objects of matching type. Returns False if the object types don't match.
        
        Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        if type(self) is not type(other):
            return False

        return self.volume == other.volume

    def __lt__(self, other: Shape) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is less than another Shape3D object. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume < other.volume

    def __gt__(self, other: Shape) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is greater than another Shape3D object. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume > other.volume

    def __ge__(self, other: Shape) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is greater than or equal to another Shape3D object. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume >= other.volume

    def __le__(self, other: Shape) -> bool | NotImplementedType:
        """
        Checks whether the volume of a Shape3D object is less than or equal to another Shape3D object. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape3D):
            return NotImplemented

        return self.volume <= other.volume    