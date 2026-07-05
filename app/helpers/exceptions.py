"""App's general exceptions.

Classes
-------
CriticalAppError(Exception)
"""


class CriticalAppError(Exception):
    """Class that represents app's critical errors.
    
    Use it to fail gracefully, i.e., communicating the error to the user via
    the UI.
    """
    pass