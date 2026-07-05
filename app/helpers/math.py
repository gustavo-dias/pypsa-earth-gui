"""Mathematical helpers.

Functions
---------
is_number(value: Any) -> bool \\
convert_scientific_to_float(value: Any) -> float
"""

from math import isinf
from typing import Any


def is_number(value: Any) -> bool:
    """Checks whether or not value is a number.
    
    It converts value to int as in int(value); returns True if the operation
    succeeds; tries to convert to float if it fails as in float(value); returns
    True if it succeeds, False otherwise.

    Special cases 'inf' and '-inf' return False (i.e. they are not treated as
    numbers by the app).

    Boolean values True and False evaluate to number (i.e. return True) since
    they are a subtype of integer in Python.

    Parameters
    ----------
    value: Any
        The value to be tested.
    
    Returns
    -------
    bool
        Whether or not value is a number.
    """
    try:
        _ = int(value)
    except Exception:
        try:
            result = float(value)
        except Exception:
            return False
        else:
            # infinities are not treated as numbers by the app, they are shown
            # as text in the UI
            if isinf(result):   
                return False
            return True
    else:
        return True


def convert_scientific_to_float(value: Any) -> float | Any:
    """Convert a number in scientific notation to float.
    
    The conversion only happens if (a) is_number(value) returns True, (b)
    isinstance(value, str) returns True and (c) the char 'e' is in value;
    otherwise, returns value. 
    
    E.g.: '1e-6' and '1e15' return as float; 'tree' returns 'tree'.

    Parameters
    ----------
    value: Any
        The number to be converted to float.

    Returns
    -------
    float
        The number value as a float.
    Any
        Otherwise.
    """
    if is_number(value) and isinstance(value, str) and ('e' in value):
        return float(value)
    return value