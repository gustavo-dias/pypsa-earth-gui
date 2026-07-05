"""App's configuration actions.

Classes
-------
ConfigActions()

Functions
---------
get_available_configuration_actions(path: Path) -> list[str]
"""

from pathlib import Path

from app.config.constants import CONFIG_FILES_EXTENSION
from app.config.files import ConfigFiles, ConfigTemplateFiles
from app.helpers.exceptions import CriticalAppError
from app.helpers.files import get_files_of_type_in


class ConfigActions():
    """Class that holds an enumeration of PyPSA-Earth configuration actions.
    
    Entries:
        - CREATE: allows the user to create a new PyPSA-Earth configuration
        based on the configuration templates.
        - USE_EXISTING: allows the user to use an existing PyPSA-Earth
        configuration.
    
    Methods
    -------
    to_list(cls) -> list[str]
    """

    CREATE = "Create configuration from scratch"
    USE_EXISTING = "Use existing configuration"

    @classmethod
    def to_list(cls) -> list[str]:
        """Get the configuration actions.
        
        Returns
        -------
        list[str]
            A list with the textual description of the configuration actions.
        """
        return [cls.CREATE, cls.USE_EXISTING]


def get_available_configuration_actions(path: Path) -> list[str]:
    """Get available PyPSA-Earth configuration actions.

    There is two possible configuration actions depending on the existing
    configuration files in path:
    
    (a) ConfigActions.CREATE: create a new configuration from scratch using the
    configuration templates (ConfigTemplateFiles.DEFAULT,
    ConfigTemplateFiles.TUTORIAL) or;
    
    (b) ConfigActions.USE_EXISTING: use an existing configuration (i.e. an
    existing ConfigFiles.CONFIG file).

    Parameters
    ----------
    path: Path
        The path to PyPSA-Earth's installation directory.

    Returns
    -------
    list[str]
        A list with the available configuration actions.

    Raises
    ------
    CriticalAppError
        If the expected configuration files are not found in path.
    """
    files: list = get_files_of_type_in(CONFIG_FILES_EXTENSION, path)

    if set(ConfigFiles.to_list()) <= set(files):
        return ConfigActions.to_list()
    elif set(ConfigTemplateFiles.to_list()) <= set(files):
        return [ConfigActions.CREATE]
    else:
        raise CriticalAppError(
            'get_available_configuration_actions(): expected configuration '
            'files are not found in path.'
        )
