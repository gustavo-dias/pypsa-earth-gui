"""App's configuration form widgets display functions.

Functions
---------
display_widget_recursively(parameter: Parameter, visited_parameters: set = None) -> None
"""

from pathlib import Path

import streamlit as st

from app.config.form.widgets.metadata import get_widget_metadata_for
from app.config.parameters import Parameter
from app.config.navigation import parameter_was_not_visited
from app.helpers.logging import get_logger_named
from app.helpers.ui.widgets import display_widget_for


logger = get_logger_named(Path(__file__).stem)


def display_widget_recursively(
        parameter: Parameter,
        visited_parameters: set = None,
    ) -> None:
    """Display parameter's widget.
    
    It runs a depth-first navigation recursively, meaning that if 
    parameter.value is a dict, it calls itself passing each of parameter's
    childs one at a time.

    Parameters
    ----------
    parameter: Parameter
        A PyPSA-Earth parameter object.
    visited_parameters: set
        A set containing the visited parameters; used to avoid revisiting when
        backtracking.
    
    Returns
    -------
    None
    """
    if visited_parameters is None:
        visited_parameters = set()

    visited_parameters.add(parameter)

    if isinstance(parameter.value, dict):
        with st.expander(parameter.name.upper()):
            with st.container(
                horizontal=True,
                horizontal_alignment='distribute',
            ):            
                for child_name, child_value in parameter.value.items():
                    child_parameter = Parameter(
                        child_name,
                        child_value,
                        parameter.unique_id_prefix,
                        parameter.hierarchy,
                    )
                    if parameter_was_not_visited(
                        child_parameter,
                        visited_parameters
                    ):
                        display_widget_recursively(
                            child_parameter,
                            visited_parameters,
                        )
    else:
        parameter.widget_metadata = get_widget_metadata_for(parameter)
        display_widget_for(parameter)
