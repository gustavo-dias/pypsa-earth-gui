"""App's UI messaging helpers.

Functions
---------
display_as_error(message: str) -> None \\
display_as_warning(message: str) -> None
"""

import streamlit as st


def display_as_error(message: str) -> None:
    """Display message as an error.
    
    The message is rendered centered in the screen.

    Parameters
    ----------
    message: str
        The string to displayed in the screen.
    
    Returns
    -------
    None
    """
    _, col_2, _ = st.columns([0.2, 0.6, 0.2])
    col_2.error(message, icon=':material/error:')


def display_as_warning(message: str) -> None:
    """Display message as a warning.
    
    The message is rendered centered in the screen.

    Parameters
    ----------
    message: str
        The string to displayed in the screen.
    
    Returns
    -------
    None
    """
    _, col_2, _ = st.columns([0.2, 0.6, 0.2])
    col_2.warning(message, icon=':material/warning:')
