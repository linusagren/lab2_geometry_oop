from typing import Any


def validate_number_type(value: Any) -> int | float:
    """
    Returns value if it's an int or float.

    Raise TypeError if not.
    """
    if not isinstance(value, int | float) or isinstance(value, bool):
        raise TypeError(f"Value must be float or int, not {type(value).__name__}.")
    return value

def validate_positive_number(value: Any) -> int | float:
    """
    Returns value if it's greater than 0.
    
    Raise ValueError if 0 or less.
    
    Raise TypeError if type is not int | float.
    """
    value = validate_number_type(value)
    if value <= 0:
        raise ValueError(f"Value must be bigger than 0, not {value}.")
    return value

def validate_number(value: Any) -> int | float:
    """
    Returns value if greater than 0 and of type int or float.
    """
    value = validate_positive_number(value)
    value = validate_number_type(value)
    return value