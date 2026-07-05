"""App's configuration data I/O functions.

Functions
---------
save_to_file(config_file_path: Path) -> None
"""

from yaml import dump
from pathlib import Path

from app.session_state.gets import get_config_data_from_ss


def save_to_file(config_file_path: Path) -> None:
    """Save the configuration data in the file config_file_path.
    
    The configuration data is retrieved from the app's session state via
    function get_config_data_from_ss().

    The data is structured as in an YAML file using the yaml.dump() function.

    Parameters
    ----------
    config_file_path: Path
        The path to the file where the configuration data must be persisted.
    
    Returns
    -------
    None
    """
    with open(config_file_path, 'w') as config_file:
        dump(
            get_config_data_from_ss(),
            config_file,
            default_flow_style=False,
            indent=2,
            sort_keys=False,
        )
