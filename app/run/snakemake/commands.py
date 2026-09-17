"""Snakemake run commands.

This module provides a function that builds valid PyPSA-Earth snakemake
commands.

Functions
---------
get_snakemake_run_command(
    folder_path: Path,
    getter_snakemake_rules: Callable[[Path], list[str]],
) -> str:
"""

import streamlit as st

from os import cpu_count
from pathlib import Path
from typing import Callable

from app.run.constants import CORES_INPUT_HELPER, CORES_INPUT_LABEL
from app.run.constants import DRYRUN_CHECKBOX_LABEL, COMMAND_INPUT_LABEL
from app.run.constants import EXTRA_ARGS_HELPER, EXTRA_ARGS_LABEL
from app.run.constants import RULES_SELECTBOX_HELPER, RULES_SELECTBOX_LABEL


def get_snakemake_run_command(
        folder_path: Path,
        getter_snakemake_rules: Callable[[Path], list[str]],
    ) -> str:
    """Get a valid PyPSA-Earth snakemake run command.
    
    Format: 'snakemake -j {cores} [-n] [other_args] rule'.

    Parameters
    ----------
    folder_path: Path,
        The path to PyPSA-Earth's local installation.
    getter_snakemake_rules: Callable[[Path], list[str]],
        A callable to retrieve the snakemake rules from PyPSA-Earth's
        snakemake file.

    Returns
    -------
    str
        A valid executable snakemake command.
    """
    col_1, col_2, col_3, col_4 = st.columns((0.15,0.15,0.35,0.35))
    dry_run: bool = col_1.checkbox(DRYRUN_CHECKBOX_LABEL)
    cores: float = col_2.number_input(
        CORES_INPUT_LABEL,
        min_value=1,
        max_value=cpu_count(),
        step=1,
        help=CORES_INPUT_HELPER,
    )
    extra_commands: str = col_3.text_input(
        EXTRA_ARGS_LABEL,
        help=EXTRA_ARGS_HELPER,
    )
    selected_rule: str | None = col_4.selectbox(
        RULES_SELECTBOX_LABEL,
        options=getter_snakemake_rules(folder_path),
        accept_new_options=True,
        help=RULES_SELECTBOX_HELPER,
    )

    cmd: str = f"snakemake -j {cores} "
    if dry_run:
        cmd = cmd + "-n "
    if extra_commands.strip() != "":
        cmd = cmd + extra_commands.strip() + " "
    cmd = cmd + selected_rule 

    return st.text_input(COMMAND_INPUT_LABEL, value=cmd, disabled=True)
