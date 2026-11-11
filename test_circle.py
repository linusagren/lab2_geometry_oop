from circle import Circle
from math import pi
from pytest import raises, approx, fixture, mark

@fixture
def circle():
    return Circle(5)

@fixture
def circle_trio():
    return Circle(5, 2, 1), Circle(2, 1, 9), Circle(2, 4, 9)

def test_valid_init():
    c1 = Circle(5)
    
    assert c1.radius == 5
    assert c1.x == 0
    assert c1.y == 0

@mark.parametrize("x, y", [
    (1, 3),
    (0, 0),
    (-2, -5),
    (5.23, -5.12)
])
def test_valid_init_coordinates(x, y):
    assert Circle(5, x, y)

def test_invalid_zero_init():
    with raises(ValueError):
        Circle(0)

def test_invalid_negative_init():
    with raises(ValueError):
        Circle(-5)

def test_invalid_string_init():
    with raises(TypeError):
        Circle("one")

    with raises(TypeError):
        Circle(5, 4, "three")

    with raises(TypeError):
        Circle(5, "four", 3)

def test_invalid_boolean_init():
    with raises(TypeError):
        Circle(True)

    with raises(TypeError):
        Circle(5, False, 3)

    with raises(TypeError):
        Circle(5, 1, True)

def test_valid_float_init():
    c1 = Circle(2.32)
    assert c1.radius == 2.32

def test_invalid_coordinate_assignment(circle):
    with raises(AttributeError):
        circle.x = 5
    assert circle.x == 0

    with raises(AttributeError):
        circle.y = 2
    assert circle.y == 0

@mark.parametrize("radius, expected", [
    (0, ValueError),
    (-5, ValueError),
    ("2", TypeError),
    (True, TypeError)
])
def test_invalid_radius_assignment(circle, radius, expected):
    with raises(expected):
        circle.radius = radius
    assert circle.radius == 5

def test_valid_radius_assignment(circle):
    circle.radius = 6
    assert circle.radius == 6

    circle.radius = 4.21
    assert circle.radius == 4.21

def test_area(circle):
    assert circle.area == approx(78.5398)

def test_perimeter(circle):
    assert circle.perimeter == approx(31.4159)

def test_translate(circle):
    circle.translate(-3, 2)
    assert circle.x == -3
    assert circle.y == 2
    assert circle.radius == 5

    circle.translate(5, -15)
    assert circle.x == 2
    assert circle.y == -13
    assert circle.radius == 5

def test_unit_circle(circle):
    assert circle.is_unit_circle() == False

    circle.radius -= 4
    assert circle.is_unit_circle() == True

    c2 = Circle(1)
    assert c2.is_unit_circle() == True

    c2.radius += 1
    assert c2.is_unit_circle() == False

def test_dunder_repr():
    c1 = Circle(5, 2, 1)
    assert repr(c1) == "Circle(5, 2, 1)"

    c1.translate(2, 1)
    assert repr(c1) == "Circle(5, 4, 2)"

    c1.radius = 4
    assert repr(c1) == "Circle(4, 4, 2)"

def test_dunder_str():
    c1 = Circle(2, 1, 8)
    assert str(c1) == "A circle with the radius 2 on position (1, 8)"

    c1.translate(4, -2)
    assert str(c1) == "A circle with the radius 2 on position (5, 6)"

    c1.radius = 1
    assert str(c1) == "A circle with the radius 1 on position (5, 6)"

def test_dunder_eq(circle_trio):
    c1, c2, c3 = circle_trio

    assert c1 != c2
    assert c2 == c3
    assert c1 != "..."
    assert c1 != 5
    assert c1 != True

def test_dunder_lt(circle_trio):
    c1, c2, c3 = circle_trio

    assert not c1 < c3
    assert c2 < c1
    assert not c2 < c3

def test_dunder_gt(circle_trio):
    c1, c2, c3 = circle_trio

    assert c1 > c2
    assert not c2 > c1
    assert not c2 > c3

def test_dunder_ge(circle_trio):
    c1, c2, c3 = circle_trio

    assert c1 >= c2
    assert c2 >= c3
    assert not c2 >= c1

def test_dunder_le(circle_trio):
    c1, c2, c3 = circle_trio

    assert not c1 <= c2
    assert c2 <= c3
    assert c2 <= c1