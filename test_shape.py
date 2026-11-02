from pytest import raises
from math import pi
from shape import Shape
from shape2d import Shape2D
from circle import Circle
from rectangle import Rectangle

def test_abstraction():
    with raises(TypeError, match=r"abstract class Shape2D"): # Match more specifically as a safeguard
        Shape2D(1, 5)

def test_valid_shape_init():
    s1 = Shape(4, 7)

    assert s1.x == 4
    assert s1.y == 7

def test_shape_comparisons():
    c1 = Circle(5)
    r1 = Rectangle(2, 4)

    assert not r1 == c1
    assert r1 < c1
    assert not r1 > c1

    c2 = Circle(2)
    r2 = Rectangle(4, pi)

    assert c2 != r2
    assert c2 >= r2
    assert c2 <= r2

def test_invalid_translate():
    c1 = Circle(5, 4, 1)
    
    with raises(TypeError):
        c1.translate("...", 3)
    assert c1.x == 4
    assert c1.y == 1
    
    with raises(TypeError):
        c1.translate(3, "...")
    assert c1.x == 4
    assert c1.y == 1