"""User input validation helpers.

Functions
---------
is_pypsa_earth_folder_path(folder_path: Path) -> bool
"""

from pathlib import Path

from app.config.constants import CONFIG_FILES_EXTENSION
from app.config.files import ConfigFiles, ConfigTemplateFiles
from app.helpers.files import get_files_of_type_in


def is_pypsa_earth_folder_path(folder_path: Path) -> bool:
    """Check if folder_path points to a valid PyPSA-Earth folder.
    
    A valid PyPSA-Earth folder contains either (a) the three valid ConfigFiles
    or (b) at least both the ConfigTemplateFiles; return True in these two
    cases, False otherwise.
    
    Parameters
    ----------
    folder_path: Path
        To folder path to test for having the PyPSA-Earth configuration files.
    
    Returns
    -------
    bool
        Whether or not folder_path is a valid PyPSA-Earth folder.
    """
    files: list = get_files_of_type_in(CONFIG_FILES_EXTENSION, folder_path)

    if set(ConfigFiles.to_list()) <= set(files):
        return True
    elif set(ConfigTemplateFiles.to_list()) <= set(files):
        return True
    else:
        return False

