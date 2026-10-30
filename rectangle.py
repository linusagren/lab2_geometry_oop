from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        super().__init__(x, y)

        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if not isinstance(value, float | int) or isinstance(value, bool):
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if not isinstance(value, float | int) or isinstance(value, bool):
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        return self.width == self.height

    def __str__(self) -> str:
        return f"A rectangle with width {self.width} and height {self.height} on position ({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height}, {self.x}, {self.y})"