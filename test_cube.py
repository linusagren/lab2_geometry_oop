from pytest import raises
from cube import Cube

def test_valid_init():
    assert Cube(5)

def test_invalid_init():
    with raises(TypeError):
        Cube("...")

    with raises(TypeError):
        Cube(True)

    with raises(ValueError):
        Cube(0)
    with raises(ValueError):
        Cube(-5)

def test_valid_side_length_assignment():
    c1 = Cube(5, 3, 1, 5)

    c1.edge_length = 3
    assert c1.edge_length == 3
    assert c1.x == 3
    assert c1.y == 1
    assert c1.z == 5

    c1.edge_length += 2
    assert c1.edge_length == 5
    assert c1.x == 3
    assert c1.y == 1
    assert c1.z == 5

def test_invalid_side_length_assignment():
    c1 = Cube(5, 3, 1, 5)

    with raises(ValueError):
        c1.edge_length = 0
    assert c1.x == 3
    assert c1.y == 1
    assert c1.z == 5
    
    with raises(ValueError):
        c1.edge_length = -4
    assert c1.x == 3
    assert c1.y == 1
    assert c1.z == 5

def test_surface_area():
    c1 = Cube(5, 3, 1, 5)
    assert c1.surface_area == 150

    c1.edge_length = 12
    assert c1.surface_area == 864

def test_volume():
    c1 = Cube(5, 3, 1, 5)
    assert c1.volume == 125

    c1.edge_length = 15
    assert c1.volume == 3375

def test_dunder_str():
    c1 = Cube(5, 3, 1, 5)
    assert str(c1) == "A cube with an edge length of 5 on position (3, 1, 5)."

    c1.translate(4, 2, 3)
    assert str(c1) == "A cube with an edge length of 5 on position (7, 3, 8)."

def test_dunder_repr():
    c1 = Cube(5, 3, 1, 5)
    assert repr(c1) == "Cube(5, 3, 1, 5)"

    c1.translate(1, -4, -3)
    assert repr(c1) == "Cube(5, 4, -3, 2)"