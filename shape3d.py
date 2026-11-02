from shape import Shape
from abc import abstractmethod

class Shape3D(Shape):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y)

        if not isinstance(z, float | int) or isinstance(z, bool):
            raise TypeError(f"'z' must be int or float, not {type(z).__name__}.")

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
        if not isinstance(dz, int | float) or isinstance(dz, bool):
            raise TypeError(f"'dz' must be int or float, not {type(dz).__name__}.")
        
        super().translate(dx, dy)
        self._z = self.z + dz