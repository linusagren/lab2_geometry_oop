import matplotlib
from pytest import raises, fixture
from rectangle import Rectangle
from shape2dplotter import Shape2DPlotter
from circle import Circle

@fixture
def shapes():
    return Rectangle(2, 2, 3, 1), Rectangle(2, 4, -5, 0), Rectangle(2, 1, 0, 0), Circle(2, 6, 0)

@fixture
def plot(shapes):
    return Shape2DPlotter.plot2d(*shapes)

def test_valid_fig_axes(plot):
    fig, axes = plot

    assert type(fig) == matplotlib.figure.Figure
    assert type(axes) == matplotlib.axes.Axes

def test_validate_patch_count(plot):
    fig, axes = plot

    assert len(axes.patches) == 4

def test_validate_shape_attributes(plot, shapes):
    fig, axes = plot

    for original, patch in zip(shapes, axes.patches):
        assert (isinstance(original, Rectangle) and isinstance(patch, matplotlib.patches.Rectangle)) or (isinstance(original, Circle) and isinstance(patch, matplotlib.patches.Circle))

        if isinstance(original, Rectangle):
            assert original.width == patch.get_width()
            assert original.height == patch.get_height()

        if isinstance(original, Circle):
            assert original.radius == patch.get_radius()
        
        assert original.x == patch.get_center()[0]
        assert original.y == patch.get_center()[1]

def test_equal_aspect_ratio(plot):
    fig, axes = plot

    assert axes.get_box_aspect() == 1.0 # Keeps plotting area square
    assert axes.get_aspect() == 1.0 # Prevents deformed shapes

def test_invalid_init_float():
    with raises(TypeError):
        Shape2DPlotter.plot2d(5.95)

def test_invalid_init_int():
    with raises(TypeError):
        Shape2DPlotter.plot2d(5)

def test_invalid_init_boolean():
    with raises(TypeError):
        Shape2DPlotter.plot2d(True)

def test_invalid_init_string():
    with raises(TypeError):
        Shape2DPlotter.plot2d("...")