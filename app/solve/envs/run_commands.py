"""Python environment run commands.


Functions
---------
get_environment_run_command(
        pypsa_earth_folder_path: Path,
        getter_env_mngrs: Callable[[list[str]], list[str]],
        getter_envs: Callable[[str], list[str] | None],
) -> str | None
"""

import streamlit as st

from pathlib import Path
from typing import Callable

from app.helpers.ui.messages import display_as_error
from app.solve.envs.managers import EnvManager


def get_environment_run_command(
        pypsa_earth_folder_path: Path,
        getter_env_mngrs: Callable[[list[str]], list[str]],
        getter_envs: Callable[[str], list[str] | None],
        ) -> str | None:
    """Get the command to run a python environment in pypsa_earth_folder_path.
    
    Command format: 'env_mngr run -n env_name --cwd pypsa_earth_folder_path'.

    For example: 'conda run -n pypsa-earth --cwd /path/to/pypsa-earth/'

    Parameters
    ----------
    pypsa_earth_folder_path: Path
        The local path to PyPSA-Earth installation.
    getter_env_mngrs: Callable[[list[str]], list[str]]
        A callable that fetchs locally installed python environment managers.
    getter_envs: Callable[[str], list[str] | None]
        A callable that returns local python environments for a given python
        environment manager.

    Returns
    -------
    str | None
        A string containing the execute command. None in case no environment
        manager is detected or there is an error retrieving the available
        existing environments.
    """
    python_env_managers: list[str] = getter_env_mngrs(EnvManager.to_list())

    if len(python_env_managers) == 0:
        display_as_error(
            "No Python environment manager installed. Check your PyPSA-Earth "
            "installation."
        )
        return None
    else:
        col_1, col_2 = st.columns((0.5, 0.5))
        selected_env_mngr: str = col_1.selectbox(
            label="Manager:",
            options=python_env_managers,
        )
        python_envs: list[str] | None = getter_envs(selected_env_mngr)
        if python_envs is not None:
            selected_env: str | None = col_2.selectbox( # type: ignore
                label="PyPSA-Earth Environment:",
                options=python_envs,
            )
            cmd = f"{selected_env_mngr} run -n {selected_env} "
            return cmd + f"--cwd {pypsa_earth_folder_path}" 
        else:
            col_2.error(
                "Could not retrieve existing Python environments for "
                f"{selected_env_mngr}. Try again or contact the PyPSA-Earth "
                "GUI support team."
            )
            return None
