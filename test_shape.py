from pytest import raises, approx
from math import pi
from shape import Shape
from circle import Circle
from rectangle import Rectangle

def test_abstraction():
    with raises(TypeError, match=r"abstract class Shape"): # Match more specifically as a safeguard
        s = Shape(1, 5)

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