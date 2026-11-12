from shape import Shape
from abc import abstractmethod
from types import NotImplementedType

class Shape2D(Shape):
    """
    Abstract superclass for shared and required properties of the Rectangle and Circle subclasses.
    """
    @property
    @abstractmethod
    def area(self) -> float:
        """
        Adds area as a requirement for subclasses.
        """
        ...

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """
        Adds perimeter as a requirement for subclasses.
        """
        ...

    def __eq__(self, other) -> bool | NotImplementedType:
        """
        Compares the areas between two Shape objects of matching type. Returns False if the object types don't match.
        
        Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented

        if type(self) is not type(other):
            return False

        return self.area == other.area

    def __lt__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is less than another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented

        return self.area < other.area

    def __gt__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is greater than another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented

        return self.area > other.area

    def __ge__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is greater than or equal to another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented

        return self.area >= other.area

    def __le__(self, other) -> bool | NotImplementedType:
        """
        Checks whether the area of a Shape object is less than or equal to another. Unsupported object types return NotImplemented.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented

        return self.area <= other.area