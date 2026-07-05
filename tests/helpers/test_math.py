"""Tests for module math.py"""

from app.helpers.math import is_number, convert_scientific_to_float


def test_is_number() -> None:
    """"""
    # ints
    assert is_number(0)
    assert is_number(1)

    # floats
    assert is_number(0.0)
    assert is_number(1.0)

    # non-boolean floats
    assert is_number(6.6)
    assert is_number(-6.6)

    # numbers as strings
    assert is_number('1')
    assert is_number('0.0')

    # boolean (True and False) is a subtype of integer in python 
    # https://docs.python.org/3/reference/datamodel.html#numbers-integral)
    assert is_number(False)
    assert is_number(True)

    # infinities (are not treated as numbers by the app, rather as text)
    assert not is_number('inf')
    assert not is_number('-inf')

    # other types
    assert not is_number('string')  # string
    assert not is_number([1])       # list
    assert not is_number((1,))      # tuple
    assert not is_number({1: 2})    # dict


def test_convert_scientific_to_float() -> None:
    """"""
    assert isinstance(convert_scientific_to_float('1e-6'), float)     # scienti
    assert isinstance(convert_scientific_to_float('1e15'), float)     # scienti
    assert isinstance(convert_scientific_to_float(6.6), float)        # float
    assert not isinstance(convert_scientific_to_float('6.6'), float)  # str
    assert not isinstance(convert_scientific_to_float('tree'), float) # str
    assert not isinstance(convert_scientific_to_float(6), float)      # int