from pytest import fixture, raises
from circle import Circle
from rectangle import Rectangle
from shape2d import Shape2D

@fixture
def shapes():
    return Rectangle(4, 4), Circle(5)

def test_invalid_direct_instantiation():
    with raises(TypeError):
        shape2d = Shape2D()

def test_dunder_eq(shapes):
    r1, c1 = shapes
    
    assert r1 != c1

def test_dunder_lt(shapes):
    r1, c1 = shapes

    assert r1 < c1
    assert not c1 < r1
    
def test_dunder_gt(shapes):
    r1, c1 = shapes

    assert not r1 > c1
    assert c1 > r1

def test_dunder_ge(shapes):
    r1, c1 = shapes

    assert not r1 >= c1
    assert c1 >= r1

def test_dunder_le(shapes):
    r1, c1 = shapes

    assert r1 <= c1
    assert not c1 <= r1