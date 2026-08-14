"""App's session state get functions.

Functions
---------
get_folder_path_from_ss() -> Path | None \\
get_save_button_disabled_from_ss() -> bool \\
get_ui_config_metadata_from_ss() -> dict \\
get_config_data_from_ss() -> dict \\
get_unsaved_changes_from_ss() -> bool \\
get_is_solving_from_ss() -> bool \\
"""

import streamlit as st

from pathlib import Path

from app.session_state.constants import _SS_CONFIG_DATA_KEY
from app.session_state.constants import _SS_FOLDER_PATH_KEY
from app.session_state.constants import _SS_SAVE_BUTTON_DISABLED_KEY
from app.session_state.constants import _SS_UI_CONFIG_METADATA_KEY
from app.session_state.constants import _SS_UNSAVED_CHANGES_KEY
from app.session_state.constants import SS_IS_SOLVING_KEY


def get_folder_path_from_ss() -> Path | None:
    """Get the PyPSA-Earth folder path from the app's session state.
     
    Returns None (by default) in case no folder path has been saved into the
    session state yet. No reason to halt the app's execution with a KeyError
    exception.

    Returns
    -------
    Path
        PyPSA-Earth's (local) folder path.
    None
        No folder path saved in the app's session state.
    """
    return st.session_state.get(_SS_FOLDER_PATH_KEY, None)


def get_save_button_disabled_from_ss() -> bool:
    """Get the save button disabled flag from the app's session state.
    
    Return True (i.e. save button disabled) by default in case the flag has not
    been set before. No reason to halt the app's execution with a KeyError
    exception.

    Returns
    -------
    bool
        Whether or not the save configuration button is disabled.
    """
    return st.session_state.get(_SS_SAVE_BUTTON_DISABLED_KEY, True)


def get_ui_config_metadata_from_ss() -> dict:
    """Get the UI configuration metadata from the app's session state.
    
    Returns
    -------
    dict
        A dictionary containing the UI configuration metadata.

    Raises
    ------
    KeyError
        If the ui config metadata has not been saved to the session state
        before invoking this function.
    """
    return st.session_state[_SS_UI_CONFIG_METADATA_KEY]


def get_config_data_from_ss() -> dict:
    """Get the configuration data from the app's session state.
    
    Raises
    ------
    KeyError:
        If the config data has not been saved to the session state before
        invoking this function.
    """
    return st.session_state[_SS_CONFIG_DATA_KEY]


def get_unsaved_changes_from_ss() -> bool:
    """Get the unsaved changes flag from the app's session state.
    
    Return False (i.e. no unsaved changes) by default in case the flag has not
    been set before invoking this function. No reason to halt the app's
    execution with a KeyError exception.

    Returns
    -------
    bool
        Whether or not there are unsaved changes in the configuration.
    """
    return st.session_state.get(_SS_UNSAVED_CHANGES_KEY, False)


def get_is_solving_from_ss() -> bool:
    """Get the is running flag from the app's session state.

    Return False (i.e. is not solving) by default in case the flag has not
    been set before invoking this function.

    Returns
    -------
    bool
        Whether or not PyPSA-Earth is solving a model. i.e., is running.
    """
    return st.session_state.get(SS_IS_SOLVING_KEY, False)