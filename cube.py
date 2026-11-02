from shape3d import Shape3D

class Cube(Shape3D):
    def __init__(self, edge_length: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y, z)

        self.edge_length = edge_length

    @property
    def edge_length(self) -> float:
        return self._edge_length

    @edge_length.setter
    def edge_length(self, value: float) -> None:
        if not isinstance(value, int | float) or isinstance(value, bool):
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        self._edge_length = value

    @property
    def surface_area(self) -> float:
        return 6 * (self.edge_length ** 2)

    @property
    def volume(self) -> float:
        return self.edge_length ** 3

    def __str__(self) -> str:
        return f"A cube with an edge length of {self.edge_length} on position ({self.x}, {self.y}, {self.z})."

    def __repr__(self) -> str:
        return f"Cube({self.edge_length}, {self.x}, {self.y}, {self.z})"