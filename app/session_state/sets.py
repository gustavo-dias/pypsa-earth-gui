"""App's session state set functions.

Functions
---------
set_folder_path_in_ss(folder_path: Path | None) -> None \\
set_ui_config_metadata_in_ss() -> None \\
set_config_data_in_ss(config_data: dict) -> None \\
set_unsaved_changes_in_ss(value: bool = False) -> None \\
set_save_button_disabled_in_ss(value: bool = True) -> None \\
set_unsavedchanges_and_savebutton_in_ss() -> None \\
set_is_solving_in_ss(value: bool = True) -> None \\
"""

import streamlit as st

from pathlib import Path
from yaml import full_load

from app.config.constants import UI_CONFIG_METADATA_FILE_NAME
from app.constants import BASE_DIR
from app.helpers.exceptions import CriticalAppError
from app.helpers.logging import get_logger_named
from app.session_state.constants import _SS_CONFIG_DATA_KEY
from app.session_state.constants import _SS_FOLDER_PATH_KEY
from app.session_state.constants import _SS_SAVE_BUTTON_DISABLED_KEY
from app.session_state.constants import _SS_UI_CONFIG_METADATA_KEY
from app.session_state.constants import _SS_UNSAVED_CHANGES_KEY
from app.session_state.constants import SS_IS_SOLVING_KEY


logger = get_logger_named(Path(__file__).stem)


def set_folder_path_in_ss(folder_path: Path | None) -> None:
    """Set the PyPSA-Earth folder path in the app's session state.
    
    Parameters
    ----------
    folder_path: Path
        The path object to be saved.
    
    Returns
    -------
    None
    """
    if isinstance(folder_path, str):
        value = Path(folder_path)
    else:
        value = folder_path
    st.session_state[_SS_FOLDER_PATH_KEY] = value


def set_ui_config_metadata_in_ss() -> None:
    """Set the ui config metadata file's content in the app's session state.
    
    It opens UI_CONFIG_METADATA_FILE_NAME and saves its content to the session
    state.

    Returns
    -------
    None

    Raises
    ------
    CriticalAppError
        If any error occurs and loading is not successfull.
    """
    try:
        with open(Path(BASE_DIR, UI_CONFIG_METADATA_FILE_NAME), 'r') as file:
            # full_load because of python specific tags
            st.session_state[_SS_UI_CONFIG_METADATA_KEY] = full_load(file)
    except Exception as exc:
        logger.error(exc)
        raise CriticalAppError(
            "set_ui_config_metadata_in_ss(): unexpected exception of type "
            f"{type(exc).__name__}."
        )


def set_config_data_in_ss(config_data: dict) -> None:
    """Set the configuration data in the app's session state.
    
    Parameters
    ----------
    config_data: dict
        The dictionary containing the configuration data to be stored in the 
        session state.
    
    Returns
    -------
    None
    """
    st.session_state[_SS_CONFIG_DATA_KEY] = config_data


def set_unsaved_changes_in_ss(value: bool = False) -> None:
    """Set the unsaved changes flag in the app's session state.
    
    The 'changes' are user modifications to the configuration data via the UI.
    Defaults to False (i.e. no unsaved changes).

    Parameters
    ----------
    value: bool
        The boolean value to be saved.
    
    Returns
    -------
    None
    """
    st.session_state[_SS_UNSAVED_CHANGES_KEY] = value


def set_save_button_disabled_in_ss(value: bool = True) -> None:
    """Set the save button disabled flag in the app's session state.
    
    Defaults to True (i.e. save button disabled).

    Parameters
    ----------
    value: bool
        The boolean value to be saved.
    
    Returns
    -------
    None
    """
    st.session_state[_SS_SAVE_BUTTON_DISABLED_KEY] = value


def set_unsavedchanges_and_savebutton_in_ss() -> None:
    """Set simultaneously the unsaved changes and save button disabled flags.
    
    Both flags are set to their default values (i.e. False and True,
    respectively). See set_unsaved_changes_in_ss() and
    set_save_button_disabled_in_ss() documentation for more details.

    Returns
    -------
    None
    """
    set_unsaved_changes_in_ss()
    set_save_button_disabled_in_ss()


def set_is_solving_in_ss(value: bool = True) -> None:
    """Set the is solving flag in the app's session state.
    
    Defaults to True (i.e. is solving).

    Parameters
    ----------
    value: bool
        The boolean value to be saved.
    
    Returns
    -------
    None
    """
    st.session_state[SS_IS_SOLVING_KEY] = value