from rectangle import Rectangle
from pytest import raises, fixture
from pytest import mark

@fixture
def rectangle():
    return Rectangle(5, 2)

@fixture
def square():
    return Rectangle(7, 7)

def test_valid_init(rectangle):
    assert rectangle.width == 5
    assert rectangle.height == 2
    assert rectangle.x == 0
    assert rectangle.y == 0

def test_invalid_zero():
    with raises(ValueError):
        Rectangle(0, 1)

    with raises(ValueError):
        Rectangle(1, 0)

def test_invalid_negative():
    with raises(ValueError):
        Rectangle(4, -2)

    with raises(ValueError):
        Rectangle(-2, 4)

def test_invalid_string():
    with raises(TypeError):
        Rectangle(4, "two")

    with raises(TypeError):
        Rectangle("one", 4)

def test_invalid_boolean():
    with raises(TypeError):
        Rectangle(6, False)

    with raises(TypeError):
        Rectangle(True, 6)

def test_valid_float():
    r1 = Rectangle(2.34, 1.95)
    assert r1.width == 2.34
    assert r1.height == 1.95

def test_read_only_assignment(rectangle):
    with raises(AttributeError):
        rectangle.x = 4

    with raises(AttributeError):
        rectangle.y = 2

@mark.parametrize("width, height, expected", [
    (0, 0, ValueError),
    ("...", "...", TypeError),
    (True, False, TypeError)
])
def test_invalid_dimension_assignment(rectangle, width, height, expected):
    with raises(expected):
        rectangle.width = width
    assert rectangle.width == 5

    with raises(expected):
        rectangle.height = height
    assert rectangle.height == 2

def test_valid_dimension_assignment(rectangle):
    rectangle.width = 3
    assert rectangle.width == 3

    rectangle.width = 7.21
    assert rectangle.width == 7.21
    
    rectangle.height = 8
    assert rectangle.height == 8

    rectangle.height = 5.24
    assert rectangle.height == 5.24

@mark.parametrize("x, y", [
    (8, 5),
    (-8, 4),
    (4, -8),
    (4.21, -8.23),
])
def test_valid_init_coordinates(x, y):
    r1 = Rectangle(2, 4, x, y)

    assert r1.x == x
    assert r1.y == y

@mark.parametrize("x, y", [
    (True, 5),
    (5, True),
    ("...", 5),
    (5, "..."),
])
def test_invalid_init_coordinates(x, y):
    with raises(TypeError):
        Rectangle(2, 4, x, y)

def test_area(rectangle):
    assert rectangle.area == 10

def test_perimeter(rectangle):
    assert rectangle.perimeter == 14

def test_translate():
    r1 = Rectangle(4, 6, 5, 8)

    r1.translate(-6, 3)
    assert r1.x == -1
    assert r1.y == 11
    assert r1.width == 4
    assert r1.height == 6

    r1.translate(2, -14)
    assert r1.x == 1
    assert r1.y == -3
    assert r1.width == 4
    assert r1.height == 6

def test_is_square():
    r1 = Rectangle(2, 2)
    r2 = Rectangle(2, 4)

    assert r1.is_square()
    assert not r2.is_square()

    r2.width = 4
    assert r2.is_square()

def test_dunder_eq(rectangle, square):
    assert rectangle != square
    assert square == Rectangle(7, 7, 5, 9)
    assert rectangle != "..."
    assert rectangle != 5
    assert rectangle != True

def test_dunder_lt(rectangle, square):
    assert rectangle < square
    assert not square < rectangle
    assert not rectangle < Rectangle(5, 2)

def test_dunder_gt(rectangle, square):
    assert not rectangle > square
    assert square > rectangle
    assert not rectangle > Rectangle(5, 2)

def test_dunder_ge(rectangle, square):
    assert not rectangle >= square
    assert square >= rectangle
    assert rectangle >= Rectangle(5, 2)

def test_dunder_le(rectangle, square):
    assert rectangle <= square
    assert not square <= rectangle
    assert rectangle <= Rectangle(5, 2)

def test_dunder_repr():
    r1 = Rectangle(4, 2, 0, 3)
    assert repr(r1) == "Rectangle(4, 2, 0, 3)"

    r1.translate(-3, -1)
    assert repr(r1) == "Rectangle(4, 2, -3, 2)"

    r1.width = 6
    r1.height = 6
    assert repr(r1) == "Rectangle(6, 6, -3, 2)"

def test_dunder_str():
    r1 = Rectangle(4, 2, 0, 3)
    assert str(r1) == "A rectangle with width 4 and height 2 on position (0, 3)"

    r1.translate(2, 5)
    assert str(r1) == "A rectangle with width 4 and height 2 on position (2, 8)"

    r1.width = 1
    r1.height = 3
    assert str(r1) == "A rectangle with width 1 and height 3 on position (2, 8)"