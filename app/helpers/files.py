"""File helpers.

Functions
---------
get_files_of_type_in(extension: str, search_path: Path) -> list[str]
"""

from os import listdir
from pathlib import Path


def get_files_of_type_in(extension: str, search_path: Path) -> list[str]:
    """Get list of file names of type extension in search_path.
    
    Parameters
    ----------
    extension: str
        The file extension of files to be retrieved.
    search_path: Path
        The path where to search for files with extension.
    
    Returns
    -------
    list[str]
        A list of file names of type extension stored in search_path.
    """
    files: list = []
    for file in listdir(path=search_path):
        if file.endswith(extension):
            files.append(file)
    return files
