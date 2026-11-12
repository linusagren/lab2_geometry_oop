import utils
from pytest import raises, fixture, mark

@fixture
def valid_values():
    return 2, 2.23

def test_validate_number_type(valid_values):
    int_, float_ = valid_values

    assert utils.validate_number_type(int_) == 2
    assert utils.validate_number_type(float_) == 2.23

def test_invalid_validate_number_type():
    with raises(TypeError):
        utils.validate_number_type("...")
    
    with raises(TypeError):
        utils.validate_number_type(True)

def test_validate_positive_number(valid_values):
    int_, float_ = valid_values

    assert utils.validate_positive_number(int_) == 2
    assert utils.validate_positive_number(float_) == 2.23

@mark.parametrize("value, expected", [
    (0, ValueError),
    (-5, ValueError),
    (float("nan"), ValueError),
    ("...", TypeError),
    (True, TypeError),
])
def test_invalid_validate_positive_number(value, expected):
    with raises(expected):
        utils.validate_positive_number(value)

def test_valid_number(valid_values):
    int_, float_ = valid_values
    
    assert utils.validate_number(int_) == 2
    assert utils.validate_number(float_) == 2.23

@mark.parametrize("value, expected", [
    (0, ValueError),
    (-5, ValueError),
    (float("nan"), ValueError),
    ("...", TypeError),
    (True, TypeError),
])
def test_invalid_validate_number(value, expected):
    with raises(expected):
        utils.validate_number(value)