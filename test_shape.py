from pytest import fixture, mark, raises
from shape import Shape

@fixture
def shape():
    return Shape(4, 7)

def test_valid_shape_init(shape):
    shape_2 = Shape()

    assert shape.x == 4
    assert shape.y == 7
    assert shape_2.x == 0
    assert shape_2.y == 0

@mark.parametrize("x, y", [
    (True, 5),
    (5, True),
    ("...", 5),
    (5, "..."),
])
def test_invalid_shape_init_coordinates(x, y):
    with raises(TypeError):
        Shape(x, y)

def test_read_only_assignment(shape):
    with raises(AttributeError):
        shape.x = 3
    assert shape.x == 4

    with raises(AttributeError):
        shape.y = 2
    assert shape.y == 7

def test_translate(shape):
    shape.translate(-6, 3)
    assert shape.x == -2
    assert shape.y == 10

    shape.translate(2, -14)
    assert shape.x == 0
    assert shape.y == -4