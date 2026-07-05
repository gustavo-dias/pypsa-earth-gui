"""App's configuration form display functions.

Functions
---------
display_config_form_based_on(config_file_path: Path) -> bool
"""

from pathlib import Path
from yaml import safe_load

from app.config.files import ConfigFiles
from app.config.form.widgets.display import display_widget_recursively
from app.config.parameters import Parameter
from app.helpers.exceptions import CriticalAppError
from app.helpers.logging import get_logger_named
from app.session_state.gets import get_unsaved_changes_from_ss
from app.session_state.sets import set_config_data_in_ss


logger = get_logger_named(Path(__file__).stem)


def display_config_form_based_on(config_file_path: Path) -> bool:
    """Display a configuration form based on config_file_path.
    
    The config_file is a PyPSA-Earth configuration file (i.e. any entry in
    ConfigFiles) that will serve as reference to build the UI configuration
    form.

    Does nothing in case config_file is not a valid PyPSA-Earth config file.

    Parameters
    ----------
    config_file: Path
        A path object pointing to the reference configuration file.
    
    Returns
    -------
    bool
        Whether or not the configuration form has been properly displayed.

    Raises
    ------
    CriticalAppError:
        If any error occurs while rendering the config form.
    """
    try:
        with open(config_file_path, 'r') as config_file:
            config_data = safe_load(config_file)
            if not get_unsaved_changes_from_ss():
                set_config_data_in_ss(config_data)
            for parameter_name, parameter_value in config_data.items():
                display_widget_recursively(
                    Parameter(
                        parameter_name,
                        parameter_value,
                        ConfigFiles.get_unique_id(config_file_path)
                    ),
                    None,
                )
    except IsADirectoryError:
        # display nothing in case config_file_path is a directory
        return False
    except Exception as exc:
        logger.error(exc)
        raise CriticalAppError(
            "display_config_form_based_on(): unexpected exception of type "
            f"{type(exc).__name__}."
        )
    else:
        return True
