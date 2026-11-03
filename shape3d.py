from abc import abstractmethod
from shape import Shape
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