from shape import Shape
from pytest import raises

def test_abstraction():
    with raises(TypeError, match=r"abstract class Shape"): # Match more specifically as a safeguard
        s = Shape(1, 5)