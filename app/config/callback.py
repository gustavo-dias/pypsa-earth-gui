"""App's configuration change callbacks.

Functions
---------
save_on_change(widget_key: str) -> None
"""

import streamlit as st

from app.config.data.set import set_config_data
from app.config.parameters import Parameter
from app.session_state.gets import get_config_data_from_ss


def save_on_change(widget_key: str) -> None:
    """Save widget's new value on on_change event.
    
    This is the main callback used to save new values input by the user via the
    UI into the configuration data dictionary.

    Parameters
    ----------
    widget_key: str
        The string representing the widget of which new value must be saved.
    
    Returns
    -------
    None
    """
    set_config_data(
        get_config_data_from_ss(),
        Parameter.get_parameter_from_unique_id(
            widget_key,
            st.session_state[widget_key]
        ),
    )
