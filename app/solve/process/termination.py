"""PyPSA-Earth solve process terminations.

This module provides a function to terminate PyPSA-Earth solve processes.

Functions
---------
kill_solve_process(process: Popen[str]) -> bool
"""

from signal import SIGTERM
from os import getpgid, killpg
from subprocess import Popen


def kill_solve_process(process: Popen[str]) -> bool:
    """Terminate process.

    The process is terminated as a process group using os.killpg().

    Parameters
    ----------
    process: Popen[str]
        The process to be terminated.

    Returns
    -------
    bool
        A flag indicating whether or not the kill was successfull.
    """
    # https://alexandra-zaharia.github.io/posts/kill-subprocess-and-its-children-on-timeout-python/
    try:
        killpg(getpgid(process.pid), SIGTERM)
    except Exception:
        return False
    else:
        return True
