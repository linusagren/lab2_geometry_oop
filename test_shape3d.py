from pytest import fixture, raises
from sphere import Sphere
from cube import Cube
from shape3d import Shape3D

@fixture
def shapes():
    return Cube(4), Sphere(5)

def test_invalid_direct_instantiation():
    with raises(TypeError):
        shape3d = Shape3D()

def test_dunder_eq(shapes):
    c1, sph1 = shapes
    
    assert c1 != sph1

def test_dunder_lt(shapes):
    c1, sph1 = shapes

    assert c1 < sph1
    assert not sph1 < c1
    
def test_dunder_gt(shapes):
    c1, sph1 = shapes

    assert not c1 > sph1
    assert sph1 > c1

def test_dunder_ge(shapes):
    c1, sph1 = shapes

    assert not c1 >= sph1
    assert sph1 >= c1

def test_dunder_le(shapes):
    c1, sph1 = shapes

    assert c1 <= sph1
    assert not sph1 <= c1