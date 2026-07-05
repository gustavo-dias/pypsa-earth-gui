"""Data helpers.

Functions
---------
load_data(file_column: tuple | list[Any]) -> list[Any]
"""

from pathlib import Path
from typing import Any
from pandas import read_csv

from app.helpers.logging import get_logger_named


logger = get_logger_named(Path(__file__).stem)


def load_data(file_column: tuple | list[Any]) -> list[Any]:
    """Get the data specified in file_column tuple as a list.
    
    File_column tuple format: (file_path, column_name).
        - file_path: path to the csv file containing the data to be retrieved.
        - column_name: name of the column in file_path to be returned as a list.

    Returns (a) file_column itself if file_column is a list or (b) an empty
    list in case an error happens when reading/accessing the file storing the
    data.
    
    Parameters
    ----------
    file_column: tuple | list[Any]
        The map (file_path, column_name) to the data to be retrieved.
    
    Returns
    -------
    list[Any]
        A list containing the data content mapped by tuple file_column.
    """
    if isinstance(file_column, list):
        return file_column
    else:
        try:
            return read_csv(file_column[0])[file_column[1]].to_list()
        except Exception as exc:
            logger.error(exc)
            logger.warning(f"Unable to load data {file_column}; returning [].")
            return []
