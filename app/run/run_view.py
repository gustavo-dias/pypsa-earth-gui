"""App's run view entry.

Functions
---------
main() -> None \\
display_run_view(folder_path: Path) -> None \\
"""

import streamlit as st

from time import time
from pathlib import Path

from app.helpers.ui.messages import display_as_warning
from app.helpers.validators import is_there_a_config_yaml_in
from app.session_state.getters import get_folder_path_from_ss
from app.session_state.getters import get_is_solving_from_ss
from app.session_state.setters import set_is_solving_in_ss
from app.run.process.monitoring import is_timed_out, monitor_process
from app.run.process.commands import get_solve_command
from app.run.constants import DIVIDER_COLOR, EXECUTION_SUBHEADER_LABEL
from app.run.constants import MSG_CREATE_CONFIG_FIRST
from app.run.constants import PYTHON_ENVS_SUBHEADER_LABEL
from app.run.constants import SNAKEMAKE_SUBHEADER_LABEL
from app.run.constants import MSG_SELECT_FOLDER_FIRST
from app.run.envs.commands import get_environment_run_command
from app.run.envs.managers import get_installed_python_env_managers
from app.run.envs.python_envs import get_available_python_envs
from app.run.process.execution import get_subprocess_for
from app.run.process.termination import kill_process
from app.run.snakemake.rules import get_snakemake_solve_rules
from app.run.snakemake.commands import get_snakemake_run_command


@st.fragment()
def display_run_view(folder_path: Path) -> None:
    """Display the run view.
    
    This is a streamlit fragment.

    Parameters
    ----------
    folder_path: Path
        The path to PyPSA-Earth's local installation.
    
    Returns
    -------
    None
    """
    st.subheader(PYTHON_ENVS_SUBHEADER_LABEL, divider=DIVIDER_COLOR)
    env_cmd = get_environment_run_command(
        folder_path,
        get_installed_python_env_managers,
        get_available_python_envs
    )
    if env_cmd is None:
        return None

    st.subheader(SNAKEMAKE_SUBHEADER_LABEL, divider=DIVIDER_COLOR)
    snakemake_cmd = get_snakemake_run_command(
        folder_path,
        get_snakemake_solve_rules,
    )
   
    st.subheader(EXECUTION_SUBHEADER_LABEL, divider=DIVIDER_COLOR)
    col_1, col_2, col_3 = st.columns(
        (0.2, 0.2, 0.2),
        vertical_alignment='bottom',
        gap='large',
    )
    selected_timeout = col_1.number_input(
        "Timeout (m):",
        min_value=0,
        value=60,
        step=1,
        help="In minutes. Set to 0 for no timeout (not recommended)."
    )
    if col_2.button(
        "Run",
        use_container_width=True,
        icon=":material/play_circle:",
        disabled=get_is_solving_from_ss(),
        on_click=set_is_solving_in_ss,
    ):
        start_time = time()

        process = get_subprocess_for(get_solve_command(env_cmd, snakemake_cmd))
        if process is None:
            return None
        else:
            timed_out, elapsed_time = monitor_process(
                process,
                selected_timeout,
                start_time,
                is_timed_out,
                kill_process,
            )
            if timed_out:
                col_3.warning(
                    f"Timed out after: {(elapsed_time):.2f} (seconds)."
                )
            elif process.returncode != 0: # not timed out but error on run
                col_3.error(f"Error after: {(elapsed_time):.2f} (seconds).")
            else:  # not timed out and successful run (returncode == 0)
                col_3.success(f"Completed in: {(elapsed_time):.2f} (seconds).")


def main() -> None:
    """Entry point for the run view.
    
    Returns
    -------
    None
    """
    pypsa_earth_folder_path: Path | None = get_folder_path_from_ss()
    if pypsa_earth_folder_path is None:
        display_as_warning(MSG_SELECT_FOLDER_FIRST)
    elif not is_there_a_config_yaml_in(pypsa_earth_folder_path):
        display_as_warning(MSG_CREATE_CONFIG_FIRST)
    else:
        display_run_view(pypsa_earth_folder_path)


if __name__ == '__main__':
    main()