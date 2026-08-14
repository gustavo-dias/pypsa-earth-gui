"""PyPSA-Earth solve process execution.

This module provides a function to initialize a python subprocess containing a
PyPSA-Earth run.

Functions
---------
get_subprocess_for(command: str) -> Popen[str] | None \\
"""

from shlex import split
from subprocess import PIPE, Popen

from app.helpers.ui.messages import display_as_error
from app.session_state.sets import set_is_solving_in_ss


def get_subprocess_for(command: str) -> Popen[str] | None:
    """Get a subprocess for command.

    The command is processed by shlex.split() before subprocess creation. The
    subprocess.Popen object is created with stdout=stderr=PIPE, text=True and 
    start_new_session=True. The last flag creates a process group for simpler
    termination handling.
    
    Parameters
    ----------
    command: str
        The command to be initialized as a subprocess.

    Returns
    -------
    Popen[str] | None
        A Popen process running command. None in case of error on creating the
        subprocess.
    """
    try:
        return Popen(
            split(command),
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            start_new_session=True, # to kill all (sub)processes as a group
        )
    except Exception:
        display_as_error(
            "Unexpected error on trying to solve. Try again or contact "
            "the PyPSA-Earth GUI support."
        )
        set_is_solving_in_ss(False)
        return None
