from circle import Circle
from math import pi
from pytest import raises, approx

def test_valid_init():
    c1 = Circle(5, 1, 3)
    c2 = Circle(9)
    c3 = Circle(2, 0, -2)
    c4 = Circle(2, -5, 0)
    
    assert c1.radius == 5
    assert c1.x == 1
    assert c1.y == 3

    assert c2.radius == 9
    assert c2.x == 0
    assert c2.y == 0

    assert c3.radius == 2
    assert c3.x == 0
    assert c3.y == -2

    assert c4.radius == 2
    assert c4.x == -5
    assert c4.y == 0

def test_invalid_zero():
    with raises(ValueError):
        Circle(0)

def test_invalid_negative():
    with raises(ValueError):
        Circle(-5)

def test_invalid_string():
    with raises(TypeError):
        Circle("one")

    with raises(TypeError):
        Circle(5, 4, "three")

    with raises(TypeError):
        Circle(5, "four", 3)

def test_invalid_boolean():
    with raises(TypeError):
        Circle(True)

    with raises(TypeError):
        Circle(5, False, 3)

    with raises(TypeError):
        Circle(5, 1, True)

def test_valid_float():
    c1 = Circle(2.32)
    assert c1.radius == 2.32

def test_invalid_assignment():
    c1 = Circle(1, 5, 3)

    with raises(AttributeError):
        c1.x = 5

    with raises(AttributeError):
        c1.y = 2

def test_invalid_radius_assignment():
    c1 = Circle(3, 1, 1)

    with raises(ValueError):
        c1.radius = 0
    assert c1.radius == 3

    with raises(ValueError):
        c1.radius = -5
    assert c1.radius == 3

    with raises(TypeError):
        c1.radius = "2"
    assert c1.radius == 3

    with raises(TypeError):
        c1.radius = True
    assert c1.radius == 3

def test_valid_radius_assignment():
    c1 = Circle(3, 1, 1)

    c1.radius = 6
    assert c1.radius == 6

    c1.radius = 4.21
    assert c1.radius == 4.21

def test_area():
    c1 = Circle(5)
    assert c1.area == approx(78.5398)

def test_perimeter():
    c1 = Circle(5)
    assert c1.perimeter == approx(31.4159)

def test_translate():
    c1 = Circle(5, 0, 9)

    c1.translate(-3, 2)
    assert c1.x == -3
    assert c1.y == 11

    c1.translate(5, -15)
    assert c1.x == 2
    assert c1.y == -4

def test_unit_circle():
    c1 = Circle(5)
    assert c1.is_unit_circle() == False

    c1.radius -= 4
    assert c1.is_unit_circle() == True

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

def test_dunder_eq():
    c1 = Circle(5, 2, 1)
    c2 = Circle(2, 1, 9)
    c3 = Circle(2, 4, 9)

    assert c1 != c2
    assert c2 == c3
    assert c1 != "..."
    assert c1 != 5
    assert c1 != True