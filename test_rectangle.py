from rectangle import Rectangle
from pytest import raises, approx

def test_valid_init():
    r1 = Rectangle(2, 4)

    assert r1.width == 2
    assert r1.height == 4

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

def test_read_only_assignment():
    r1 = Rectangle(4, 6)
    
    with raises(AttributeError):
        r1.x = 4

    with raises(AttributeError):
        r1.y = 2

def test_invalid_dimension_assignment():
    r1 = Rectangle(2, 9)

    with raises(ValueError):
        r1.width = 0
    assert r1.width == 2

    with raises(ValueError):
        r1.height = 0
    assert r1.height == 9

    with raises(ValueError):
        r1.width = -3
    assert r1.width == 2

    with raises(ValueError):
        r1.height = -2
    assert r1.height == 9

    with raises(TypeError):
        r1.width = "5"
    assert r1.width == 2

    with raises(TypeError):
        r1.height = "4"
    assert r1.height == 9

    with raises(TypeError):
        r1.width = True
    assert r1.width == 2

    with raises(TypeError):
        r1.height = False
    assert r1.height == 9

def test_valid_dimension_assignment():
    r1 = Rectangle(5, 2)
    r1.width = 3
    assert r1.width == 3

    r1.width = 7.21
    assert r1.width == 7.21
    
    r1.height = 8
    assert r1.height == 8

    r1.height = 5.24
    assert r1.height == 5.24

def test_valid_init_coordinates():
    r1 = Rectangle(2, 4, 8, 5)
    r2 = Rectangle(2, 4, -8, 4)
    r3 = Rectangle(2, 4, 4, -8)
    r4 = Rectangle(2, 4, 4.21, -8.23)
    r5 = Rectangle(2, 4)

    assert r1.x == 8
    assert r1.y == 5

    assert r2.x == -8
    assert r2.y == 4

    assert r3.x == 4
    assert r3.y == -8

    assert r4.x == 4.21
    assert r4.y == -8.23

    assert r5.x == 0
    assert r5.y == 0

def test_invalid_init_coordinates():
    with raises(TypeError):
        Rectangle(2, 4, True, -8)
    
    with raises(TypeError):
        Rectangle(2, 4, 4, False)

    with raises(TypeError):
        Rectangle(2, 4, "...", 4)

    with raises(TypeError):
        Rectangle(2, 4, 5, "...")

def test_area():
    r1 = Rectangle(4, 6)
    assert r1.area == 24

def test_perimeter():
    r1 = Rectangle(4, 6)
    assert r1.perimeter == 20

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