"""App's solve view entry.

Functions
---------
main() -> None \\
display_solve_view(folder_path: Path) -> None \\
"""

import streamlit as st

from time import time
from pathlib import Path

from app.helpers.ui.messages import display_as_warning
from app.helpers.validators import is_there_a_config_yaml_in
from app.session_state.gets import get_folder_path_from_ss
from app.session_state.gets import get_is_solving_from_ss
from app.session_state.sets import set_is_solving_in_ss
from app.solve.process.monitoring import is_timed_out, monitor_process
from app.solve.process.commands import get_solve_command
from app.solve.constants import MSG_CREATE_CONFIG_FIRST
from app.solve.constants import MSG_SELECT_FOLDER_FIRST
from app.solve.envs.run_commands import get_environment_run_command
from app.solve.env_managers import get_installed_python_env_managers
from app.solve.envs.python_envs import get_available_python_envs
from app.solve.process.execution import get_subprocess_for
from app.solve.process.termination import kill_process
from app.solve.snakemake.rules import get_snakemake_rules
from app.solve.snakemake.run_commands import get_snakemake_command


@st.fragment()
def display_solve_view(folder_path: Path) -> None:
    """Display the solve view.
    
    This is a streamlit fragment.

    Parameters
    ----------
    folder_path: Path
        The path to PyPSA-Earth's local installation.
    
    Returns
    -------
    None
    """
    env_cmd = get_environment_run_command(
        folder_path,
        get_installed_python_env_managers,
        get_available_python_envs
    )
    if env_cmd is None:
        return None

    snakemake_cmd = get_snakemake_command(folder_path, get_snakemake_rules)
   
    st.subheader("Execution", divider='blue')
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
    """Entry point for the solve view.
    
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
        display_solve_view(pypsa_earth_folder_path)


if __name__ == '__main__':
    main()