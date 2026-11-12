from pytest import raises, fixture, approx, mark
from sphere import Sphere

@fixture
def sphere():
    return Sphere(5, 3, 1, 5)

@fixture
def sphere_trio():
    return Sphere(5, 3, 1, 5), Sphere(5, 1, 0, -5), Sphere(2, 1, 0, -5)

def test_valid_init():
    sph1 = Sphere(5)

    assert sph1.radius == 5
    assert sph1.x == 0
    assert sph1.y == 0
    assert sph1.z == 0

@mark.parametrize("x, y, z", [
    (1, 3, 4),
    (0, 0, 0),
    (-2, -5, -6),
    (5.23, -5.12, 3.27)
])
def test_valid_init_coordinates(x, y, z):
    sph1 = Sphere(5, x, y, z)

    assert sph1.radius == 5
    assert sph1.x == x
    assert sph1.y == y
    assert sph1.z == z

def test_valid_radius_assignment(sphere):
    sphere.radius = 3
    assert sphere.radius == 3
    assert sphere.x == 3
    assert sphere.y == 1
    assert sphere.z == 5

    sphere.radius = 5.21
    assert sphere.radius == 5.21
    assert sphere.x == 3
    assert sphere.y == 1
    assert sphere.z == 5

def test_circumference(sphere):
    assert sphere.circumference == approx(31.41, rel=1e-2)

    sphere.radius = 12
    assert sphere.circumference == approx(75.39, rel=1e-2)

# Source: https://docs.pytest.org/en/stable/reference/reference.html#pytest-approx
def test_surface_area(sphere):
    assert sphere.surface_area == approx(314.16, rel=1e-2)

    sphere.radius = 12
    assert sphere.surface_area == approx(1809.56, rel=1e-2)

def test_volume(sphere):
    assert sphere.volume == approx(523.6, rel=1e-2)

    sphere.radius = 15
    assert sphere.volume == approx(14137.17, rel=1e-2)

def test_invalid_circumference_assignment(sphere):
    with raises(AttributeError):
        sphere.circumference = 5

def test_invalid_surface_area_assignment(sphere):
    with raises(AttributeError):
        sphere.surface_area = 5

def test_invalid_volume_assignment(sphere):
    with raises(AttributeError):
        sphere.volume = 50

def test_valid_translate(sphere):
    sphere.translate(-3, 2, 6)
    assert sphere.x == 0
    assert sphere.y == 3
    assert sphere.z == 11
    assert sphere.radius == 5

    sphere.translate(5.3, -15.4)
    assert sphere.x == 5.3
    assert sphere.y == -12.4
    assert sphere.z == 11
    assert sphere.radius == 5

def test_invalid_zero_init():
    with raises(ValueError):
        Sphere(0)

def test_invalid_negative_init():
    with raises(ValueError):
        Sphere(-5)

def test_invalid_string_init():
    with raises(TypeError):
        Sphere("...")

def test_invalid_boolean_init():
    with raises(TypeError):
        Sphere(True)

@mark.parametrize("value", [
    "2", True
])
def test_invalid_coordinate_init(value):
    with raises(TypeError):
        Sphere(5, value, 0, 0)
    with raises(TypeError):
        Sphere(5, 0, value, 0)
    with raises(TypeError):
        Sphere(5, 0, 0, value)

def test_invalid_coordinate_assignment(sphere):
    with raises(AttributeError):
        sphere.x = 5
    assert sphere.x == 3

    with raises(AttributeError):
        sphere.y = 5
    assert sphere.y == 1

    with raises(AttributeError):
        sphere.z = 2
    assert sphere.z == 5

@mark.parametrize("radius, expected", [
    (0, ValueError),
    (-5, ValueError),
    ("2", TypeError),
    (True, TypeError)
])
def test_invalid_radius_assignment(sphere, radius, expected):
    with raises(expected):
        sphere.radius = radius
    assert sphere.radius == 5
    assert sphere.x == 3
    assert sphere.y == 1
    assert sphere.z == 5

@mark.parametrize("x, y, z", [
    ("...", 4, 1),
    (1, "...", 1),
    (1, 4, "..."),
    (True, 4, 5),
    (1, True, 5),
    (1, 4, True),
])
def test_invalid_translate(sphere, x, y, z):
    with raises(TypeError):
        sphere.translate(x, y, z)
    assert sphere.x == 3
    assert sphere.y == 1
    assert sphere.z == 5

def test_dunder_eq(sphere_trio): #5, 5, 2
    sph1, sph2, sph3 = sphere_trio

    assert sph1 == sph2
    assert sph1 != sph3
    assert sph1 != "..."
    assert sph1 != 5
    assert sph1 != True

def test_dunder_lt(sphere_trio):
    sph1, sph2, sph3 = sphere_trio

    assert not sph1 < sph3
    assert sph3 < sph1
    assert not sph1 < sph2

def test_dunder_gt(sphere_trio):
    sph1, sph2, sph3 = sphere_trio

    assert sph1 > sph3
    assert not sph3 > sph1
    assert not sph1 > sph2

def test_dunder_ge(sphere_trio):
    sph1, sph2, sph3 = sphere_trio

    assert sph1 >= sph3
    assert not sph3 >= sph1
    assert sph1 >= sph2

def test_dunder_le(sphere_trio):
    sph1, sph2, sph3 = sphere_trio

    assert not sph1 <= sph3
    assert sph3 <= sph1
    assert sph1 <= sph2

def test_dunder_str():
    sph1 = Sphere(5, 3, 1, 5)
    assert str(sph1) == "A sphere with radius 5 on position (3, 1, 5)."

    sph1.translate(4, 2, 3)
    assert str(sph1) == "A sphere with radius 5 on position (7, 3, 8)."

def test_dunder_repr():
    sph1 = Sphere(5, 3, 1, 5)
    assert repr(sph1) == "Sphere(5, 3, 1, 5)"

    sph1.translate(1, -4, -3)
    assert repr(sph1) == "Sphere(5, 4, -3, 2)"