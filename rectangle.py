from shape import Shape

class Rectangle(Shape):
    """
    Subclass of Shape for creating rectangles.
    """
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0) -> None:
        """
        Initializes width and height as attributes.

        x and y coordinates are initialized by the Shape superclass.
        """
        super().__init__(x, y)

        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        """
        Returns the width of a Rectangle object.
        """
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """
        Validates the type of 'value' and stores it in an instance attribute.

        Invalid types raise TypeError. Negative or zero-values raise ValueError.
        """
        if not isinstance(value, float | int) or isinstance(value, bool):
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        self._width = value

    @property
    def height(self) -> float:
        """
        Returns the height of a Rectangle object.
        """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """
        Validates the type of 'value' and stores it in an instance attribute.

        Invalid types raise TypeError. Negative or zero-values raise ValueError.
        """
        if not isinstance(value, float | int) or isinstance(value, bool):
            raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
        if value <= 0:
            raise ValueError(f"Value must be bigger than 0, not {value}.")
        self._height = value

    @property
    def area(self) -> float:
        """
        Calculates the area of a Rectangle object and returns it as a float.
        """
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        """
        Calculates the perimeter of a Rectangle object and returns it as a float.
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Checks whether a Rectangle object is a square.
        """
        return self.width == self.height

    def __str__(self) -> str:
        """
        Returns a human-readable description of a Rectangle object as a string.
        """
        return f"A rectangle with width {self.width} and height {self.height} on position ({self.x}, {self.y})"

    def __repr__(self) -> str:
        """
        Returns a Rectangle object and its values as a string.
        """
        return f"Rectangle({self.width}, {self.height}, {self.x}, {self.y})"