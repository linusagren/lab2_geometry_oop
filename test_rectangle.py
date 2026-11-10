from rectangle import Rectangle
from pytest import raises, fixture
from pytest import mark

@fixture
def rectangle():
    return Rectangle(5, 2)

def test_valid_init(rectangle):
    r1 = rectangle

    assert r1.width == 5
    assert r1.height == 2
    assert r1.x == 0
    assert r1.y == 0

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
    r1 = rectangle
    
    with raises(AttributeError):
        r1.x = 4

    with raises(AttributeError):
        r1.y = 2

@mark.parametrize("width, height, expected", [
    (0, 0, ValueError),
    ("...", "...", TypeError),
    (True, False, TypeError)
])
def test_invalid_dimension_assignment(rectangle, width, height, expected):
    r1 = rectangle
    
    with raises(expected):
        r1.width = width
    assert r1.width == 5

    with raises(expected):
        r1.height = height
    assert r1.height == 2

def test_valid_dimension_assignment(rectangle):
    r1 = rectangle

    r1.width = 3
    assert r1.width == 3

    r1.width = 7.21
    assert r1.width == 7.21
    
    r1.height = 8
    assert r1.height == 8

    r1.height = 5.24
    assert r1.height == 5.24

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
    (True, True),
    ("...", "..."),
])
def test_invalid_init_coordinates(x, y):
    with raises(TypeError):
        Rectangle(2, 4, x, 3)
    with raises(TypeError):
        Rectangle(2, 4, 3, y)

def test_area(rectangle):
    r1 = rectangle
    assert r1.area == 10

def test_perimeter(rectangle):
    r1 = rectangle
    assert r1.perimeter == 14

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