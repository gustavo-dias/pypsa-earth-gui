"""Date and time helpers.

Functions
---------
get_date_in_datetime_isoformat(date: str) -> str
"""

from datetime import datetime


def get_date_in_datetime_isoformat(date: str) -> str:
    """Get date in datetime isoformat.
    
    It is expected date to be in the following ISO 8601 pattern: YYYY-MM-DD.

    Parameters
    ----------
    date: str
        A string representing the date to be converted.
    
    Returns
    -------
    str
        The date in isoformat.
    """
    return datetime.fromisoformat(date).isoformat()
