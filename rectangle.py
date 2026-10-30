from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        super().__init__(x, y)

        self.width = width
        self.height = height

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