from pytest import raises, fixture, mark
from cube import Cube

@fixture
def cube():
    return Cube(5, 3, 1, 5)

@fixture
def cube_trio():
    return Cube(5, 3, 1, 5), Cube(5, 1, 0, -5), Cube(2, 1, 0, -5)

def test_valid_init():
    c1 = Cube(5)

    assert c1.edge_length == 5
    assert c1.x == 0
    assert c1.y == 0

@mark.parametrize("x, y, z", [
    (1, 3, 4),
    (0, 0, 0),
    (-2, -5, -6),
    (5.23, -5.12, 3.27)
])
def test_valid_init_coordinates(x, y, z):
    assert Cube(5, x, y, z)


def test_valid_edge_length_assignment(cube):
    cube.edge_length = 3
    assert cube.edge_length == 3
    assert cube.x == 3
    assert cube.y == 1
    assert cube.z == 5

    cube.edge_length = 5.21
    assert cube.edge_length == 5.21
    assert cube.x == 3
    assert cube.y == 1
    assert cube.z == 5

def test_surface_area(cube):
    assert cube.surface_area == 150

    cube.edge_length = 12
    assert cube.surface_area == 864

def test_volume(cube):
    assert cube.volume == 125

    cube.edge_length = 15
    assert cube.volume == 3375

def test_valid_translate(cube): #3, 1, 5
    cube.translate(-3, 2, 6)
    assert cube.x == 0
    assert cube.y == 3
    assert cube.z == 11
    assert cube.edge_length == 5

    cube.translate(5.3, -15.4, -4.5)
    assert cube.x == 5.3
    assert cube.y == -12.4
    assert cube.z == 6.5
    assert cube.edge_length == 5

def test_invalid_zero_init():
    with raises(ValueError):
        Cube(0)

def test_invalid_negative_init():
    with raises(ValueError):
        Cube(-5)

def test_invalid_string_init():
    with raises(TypeError):
        Cube("...")

def test_invalid_boolean_init():
    with raises(TypeError):
        Cube(True)

def test_invalid_coordinate_assignment(cube):
    with raises(AttributeError):
        cube.x = 5
    assert cube.x == 3

    with raises(AttributeError):
        cube.y = 5
    assert cube.y == 1

    with raises(AttributeError):
        cube.z = 2
    assert cube.z == 5

@mark.parametrize("edge_length, expected", [
    (0, ValueError),
    (-5, ValueError),
    ("2", TypeError),
    (True, TypeError)
])
def test_invalid_edge_length_assignment(cube, edge_length, expected):
    with raises(expected):
        cube.edge_length = edge_length
    assert cube.edge_length == 5
    assert cube.x == 3
    assert cube.y == 1
    assert cube.z == 5

@mark.parametrize("x, y, z", [
    ("...", 4, 1),
    (1, "...", 1),
    (1, 4, "..."),
    (True, 4, 5),
    (1, True, 5),
    (1, 4, True),
])
def test_invalid_translate(cube, x, y, z):
    with raises(TypeError):
        cube.translate(x, y, z)
    assert cube.x == 3
    assert cube.y == 1
    assert cube.z == 5

def test_dunder_eq(cube_trio): #5, 5, 2
    c1, c2, c3 = cube_trio

    assert c1 == c2
    assert c1 != c3
    assert c1 != "..."
    assert c1 != 5
    assert c1 != True

def test_dunder_lt(cube_trio):
    c1, c2, c3 = cube_trio

    assert not c1 < c3
    assert c3 < c1
    assert not c1 < c2

def test_dunder_gt(cube_trio):
    c1, c2, c3 = cube_trio

    assert c1 > c3
    assert not c3 > c1
    assert not c1 > c2

def test_dunder_ge(cube_trio):
    c1, c2, c3 = cube_trio

    assert c1 >= c3
    assert not c3 >= c1
    assert c1 >= c2

def test_dunder_le(cube_trio):
    c1, c2, c3 = cube_trio

    assert not c1 <= c3
    assert c3 <= c1
    assert c1 <= c2

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