"""Python environment managers.

The module provides resources to identify locally installed python environment
managers like conda, mamba, etc.

Classes
-------
EnvManager() \\

Functions
---------
get_installed_python_env_managers(options: list[str]) -> list[str] \\
"""

from typing import Literal
from subprocess import DEVNULL, run


class EnvManager():
    """Class that holds an enumeration of Python environment managers.
    
    Entries:
        - CONDA
        - MAMBA
    
    Methods
    -------
    to_list(cls) -> list[str]
    """
    CONDA: Literal['conda'] = 'conda'
    MAMBA: Literal['mamba'] = 'mamba'

    @classmethod
    def to_list(cls) -> list[str]:
        """Get the list of python environment managers.
        
        Returns
        -------
        list[str]
            A list with the names of python environment managers.
        """
        return [cls.CONDA, cls.MAMBA]


def get_installed_python_env_managers(options: list[str]) -> list[str]:
    """Get the list of python environment managers installed locally.
    
    The function executes the command '<env_mngr_name> --version' using the
    subprocess.run() function and adds <env_mngr_name> to the list when the 
    return code is 0.

    Parameters
    ----------
    options: list[str]
        The names of existing python environment managers, e.g. mamba, conda.
    
    Returns
    -------
    list[str]
        The names of the python environment managers installed locally.
    """
    python_env_managers: list[str] = []
    for option in options:
        if run([option, '--version'], stdout=DEVNULL).returncode == 0:
            python_env_managers.append(option)
    return python_env_managers

