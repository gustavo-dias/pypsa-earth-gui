"""PyPSA-Earth solve process monitoring.

This module provides two functions to monitor a PyPSA-Earth run.

Functions
---------
monitor_process(
    process: Popen[str],
    selected_timeout: int,
    start_time: float,
    verifier_timeout: Callable[[int, float], bool]
) -> tuple[bool, float]:
is_timed_out(selected_timeout: int, start_time: float) -> bool
"""

import streamlit as st

from time import time
from subprocess import Popen
from typing import Callable, Literal

from app.helpers.ui.messages import display_as_error
from app.session_state.sets import set_is_solving_in_ss


MINUTES_TO_SECONDS: Literal[60] = 60


@st.fragment
def monitor_process(
        process: Popen[str],
        selected_timeout: int,
        start_time: float,
        verifier_timeout: Callable[[int, float], bool],
        process_terminator: Callable[[Popen[str]], bool],
    ) -> tuple[bool, float]:
    """Monitor process.
    
    Parameters
    ----------
    process: Popen[str]
        The process to be monitored.
    selected_timeout: int
        The selected time out in minutes.
    start_time: float
        The process starting time in seconds.
    verifier_timeout: Callable[[int, float], bool]
        The callable that determines whether or not the process timed out.
    process_terminator: Callable[[Popen[str]], bool]
        The callable that terminates the process in case of time out.
    
    Returns
    -------
    tuple[bool, float]
        A bool indicating whether or not the process timed out and a float 
        representing the elapsed time until the end of the monitoring.
    """
    timed_out = False
    inf_exp = st.expander("LOG")
    inf_cont = inf_exp.container(height=150, autoscroll=True, gap='xxsmall')
    try:
        while True:
            if process.stdout is not None: # i.e. if process is not silent
                output = process.stdout.readline()
                if output == '' and process.poll() is not None: # process over
                    break
                if output:
                    inf_cont.markdown(f''':blue-background[{output}]''', width="stretch")
            else: # process is silent
                if process.poll() is not None: # process over
                    break
            if verifier_timeout(selected_timeout, start_time):
                process_terminator(process)
                timed_out = True
                break
    except Exception:
        display_as_error(
            "Unexpected error during solving process. Try again or contact " \
            "the PyPSA-Earth GUI support."
        )
    finally:
        set_is_solving_in_ss(False)
        return timed_out, (time()-start_time)


def is_timed_out(selected_timeout: int, start_time: float) -> bool:
    """Check whether or not the process has timed out.

    It returns a logic AND between two conditions:
        1) selected_timeout > 0 (time out has been activated);
        2) current_time-start_time > selected_timeout*60 (elapsed greater than
        time out in seconds).

    Parameters
    ----------
    selected_timeout: int
        The value of the time out in minutes.
    start_time: float
        The process start time in seconds.
    
    Returns
    -------
    bool
        A flag indicating whether or not the process has timed out.
    """
    return ((selected_timeout > 0) and 
            (time()-start_time > selected_timeout*MINUTES_TO_SECONDS))
