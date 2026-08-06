# Author: Gustavo Dias
# E-mail: gustavodias.po@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

"""PyPSA-Earth app's UI config metadata builder.

Functions
---------
main() -> None \\
set_ui_config_metadata(ui_config_metadata: dict, parameter: Parameter) -> None \\
convert_to_bool(value: str) -> bool | Any \\
get_helper_for(context: BuilderContext, parameter: Parameter) -> str \\
get_widget_metadata_for(context: BuilderContext, parameter: Parameter) -> dict \\
update_ui_config_metadata(context: BuilderContext, parameter: Parameter, visited_parameters: set[Parameter] = None) -> None

Classes
-------
BuilderContext()
"""

from pathlib import Path
from re import search
from typing import Any
from yaml import safe_load, dump
from argparse import ArgumentParser

from app.config.constants import UI_CONFIG_METADATA_FILE_NAME
from app.config.constants import UI_METADATA_DEFAULT_ID
from app.config.parameters import Parameter
from app.constants import BASE_DIR
from app.helpers.math import is_number
from app.config.navigation import parameter_was_not_visited
from app.helpers.logging import get_logger_named
from app.helpers.ui.widgets import Metadata, WidgetType


# DATA SOURCES
# - countries: https://datahub.io/core/country-list
# TODO: find a better solution; parameter key hardcoded not a good one
_DATA_DISPATCHER: dict = {
    'countries': ('./app/config/data/sources/country_iso_code.csv', 'Code'),  
}
_DEFAULT_METADATA: dict = {
    UI_METADATA_DEFAULT_ID: {
        Metadata.WIDGET_TYPE: WidgetType.TEXT_INPUT,
        Metadata.HELPER: '',
        Metadata.DISABLED: False,
        Metadata.VISIBLE: True,
        Metadata.WIDTH: 200,
    }
}


logger = get_logger_named(Path(__file__).stem)


def set_ui_config_metadata(
        ui_config_metadata: dict,
        parameter: Parameter,
    ) -> None:
    """Update the parameter's widget metadata in ui_config_metadata.
    
    The function recursively calls itself to navigate into higher levels of the
    ui_config_metadata structure following the parameter's hierarchy. Levels:

    param1:                 <- level 0
        param2:             <- level 1
            param3:         <- level 2 \\
                . . .
                    paramN  <- level N

    Parameters
    ----------
    ui_config_metadata: dict
        The complete ui_config_metadata dictionary.
    parameter: Parameter
        A PyPSA-Earth parameter object.
    
    Returns
    -------
    None
    """
    if len(parameter.hierarchy) == 1:
        ui_config_metadata[parameter.name] = parameter.widget_metadata
    else:
        # to navigate into higher levels, pass to set_ui_config_metadata the 
        # ui_config_metadata associated with the lowest level entry (idx=0)
        # in parameter's hierarchy whilst also removing it from the hierarchy
        current_hierarchy_idx: int = 0
        current_key = parameter.hierarchy[current_hierarchy_idx]
        parameter.remove_from_hierarchy(current_hierarchy_idx)
        set_ui_config_metadata(
            ui_config_metadata[current_key],
            parameter,
        )


class BuilderContext():
    """Class that represents UI config metadata builder contexts.
    
    A context contains relevant global data for the builder application. It is
    passed throughout function calls to provide relevant global data locally.
    """

    def __init__(
            self,
            config_file_name: str,
            ui_config_metadata_file_path: Path,
            parameter_count: int = 0,
            ui_config_metadata: dict = {},
            default_visible: bool = True,
            default_disabled: bool = False,
        ) -> None:
        """Initialize a builder context object.
        
        Parameters
        ----------
        config_file_name: str
            Name of the PyPSA-Earth config file used as template for the UI.
        ui_config_metadata_file_path: Path
            Path to the PyPSA-Earth App UI configuration file.
        parameter_count: int
            Count on the number of config_file_name parameters processed.
        ui_config_metadata: dict
            The actual metadata for the UI; content to be written to 
            ui_config_metadata_file_path.
        default_visible: bool
            Default value for the widget's visible attribute.
        defaut_disabled: bool
            Default value for the widget's disabled attribute.
        """
        self.config_file_name = config_file_name
        """Name of the PyPSA-Earth config file used as template for the UI."""
        self.ui_config_metadata_file_path = ui_config_metadata_file_path
        """Path to the PyPSA-Earth App UI configuration file."""
        self.parameter_count = parameter_count
        """Count on the number of config_file_name parameters processed."""
        self.ui_config_metadata = ui_config_metadata
        """The actual metadata for the UI; content to be written to
        ui_config_metadata_file_path.
        """
        self.default_disabled = default_disabled
        """Default value for the widget's visible attribute."""
        self.default_visible = default_visible
        """Default value for the widget's disabled attribute."""
        self.helper_line_idx = -1
        """Pointer used to parse the config file and retrieve parameters' 
        helpers.
        """


def convert_to_bool(value: str | Any) -> bool | Any:
    """Get value as a bool.
    
    Expected values are 'False' or 'True', returning False or True,
    respectively; returns value otherwise.
    
    Parameters
    ----------
    value: str
        The value to be converted.
    
    Returns
    -------
    bool
        The converted value
    Any
        If value is neither the string 'False' nor 'True'.
    """
    if value == 'False':
        return False
    elif value == 'True':
        return True
    else:
        return value


def get_helper_for(context: BuilderContext, parameter: Parameter) -> str:
    """Get the UI helper for parameter.

    The helper is the text that appears when the user's cursor hovers over the
    exclamation icon. It is retrieved from inline comments in the config file,
    as in:
    
    parameter_1: value  # inline comment that becomes helper.

    Returns empty string ("") in case there is no comment.

    Parameters
    ----------
    context: BuilderContext
        The builder's context object.
    parameter: Parameter
        The PyPSA-Earth's parameter to have the helper retrieved.
    
    Returns
    -------
    str
        The string containing the helper text for parameter.
    """
    with open(context.config_file_name, 'r') as file:
        lines: list = file.readlines()
        for line_idx, line in enumerate(lines):
            if line_idx > context.helper_line_idx:
                if (search(rf'^\s*{parameter.name}:', line) and
                    search('# ', line)):
                    context.helper_line_idx = line_idx
                    helper = line.split('# ')[len(line.split('# '))-1].strip()
                    return helper.capitalize()
    return ""


def get_widget_metadata_for(
        context: BuilderContext,
        parameter: Parameter,
    ) -> dict:
    """Get the widget metadata for parameter.

    It tries to identify the parameter's value type (str, number, list, etc) to
    return an appropriate widget metadata. Returns WidgetType.TEXT_INPUT by
    default in case the type is not identified.

    Parameters
    ----------
    context: BuilderContext
        The builder's context object.
    parameter: Parameter
        The PyPSA-Earth's parameter to have the ui config metadata retrieved.
    
    Returns
    -------
    dict
        A dictionary containing parameter's widget metadata.
    """
    metadata: dict = {
        Metadata.DISABLED: context.default_disabled,
        Metadata.VISIBLE: context.default_visible,
        Metadata.WIDTH: 200,
    }

    # check for boolean first; need to convert o string before checking
    # because boolean (True, False) is a subtype of integer in python 
    # https://docs.python.org/3/reference/datamodel.html#numbers-integral)
    if (str(parameter.value) in ('False', 'True')):
        metadata[Metadata.WIDGET_TYPE] = WidgetType.CHECKBOX
        metadata.pop(Metadata.WIDTH)
    # check for numbers
    elif is_number(parameter.value):
        metadata[Metadata.WIDGET_TYPE] = WidgetType.NUMBER_INPUT
    # check for hex color using regular expressions
    elif search('^#(?:[0-9a-fA-F]{3,4}){1,2}$', str(parameter.value)):
        metadata[Metadata.WIDGET_TYPE] = WidgetType.COLOR_PICKER
        metadata.pop(Metadata.WIDTH)
    # check for lists
    elif isinstance(parameter.value, list):
        # if len(parameter.value) == 1:
        #     print(parameter.unique_id)
        #     metadata[Metadata.WIDGET_TYPE] = WidgetType.SELECTBOX
        # else:
        metadata[Metadata.WIDGET_TYPE] = WidgetType.MULTISELECT
        metadata[Metadata.OPTIONS] = _DATA_DISPATCHER.get(
            parameter.name,
            []
        )
    # check for dates with format YYYY-MM-DD
    elif search(r'\d{2,4}-\d{1,2}-\d{1,2}', str(parameter.value)):
        metadata[Metadata.WIDGET_TYPE] = WidgetType.DATE_INPUT
    # check for strings; str must be the last case or many values (that
    # match the cases above) will also evaluate to str
    elif isinstance(parameter.value, str): 
        metadata[Metadata.WIDGET_TYPE] = WidgetType.TEXT_INPUT
    # and finally everything else
    else:
        logger.warning(
            f"Returning default text_input to {parameter.name}: "
            f"{parameter.value}"
        )
        metadata[Metadata.WIDGET_TYPE] = WidgetType.TEXT_INPUT
    
    metadata[Metadata.HELPER] = get_helper_for(context, parameter)
    return metadata


def update_ui_config_metadata(
        context: BuilderContext,
        parameter: Parameter,
        visited_parameters: set[Parameter],
    ) -> None:
    """Set parameter's UI configuration metadata in context.
    
    It runs a depth-first navigation recursively in parameter if its value is a
    dict.

    Parameters
    ----------
    context: BuilderContext
        The builder's context object.
    parameter: Parameter
        The PyPSA-Earth's parameter to have the ui config metadata updated.
    visited_parameters: set[Parameter]
        The set of visisted parameters.
    
    Returns
    -------
    None
    """
    if visited_parameters is None:
        visited_parameters = set()

    visited_parameters.add(parameter)

    if isinstance(parameter.value, dict):
        for child_name, child_value in parameter.value.items():
            child_parameter = Parameter(
                child_name,
                child_value,
                ancestors=parameter.hierarchy,
            )
            if parameter_was_not_visited(child_parameter, visited_parameters):
                update_ui_config_metadata(
                    context,
                    child_parameter,
                    visited_parameters,
                )
    else:
        context.parameter_count += 1
        parameter.widget_metadata = get_widget_metadata_for(context, parameter)
        set_ui_config_metadata(
            context.ui_config_metadata,
            parameter,
        )


def main() -> None:
    """Entry point for the PyPSA-Earth App GUI config builder.
    
    Returns
    -------
    None
    """
    parser = ArgumentParser(prog='PyPSA-Earth App GUI Config Builder')
    parser.add_argument(
        'config_file_name',
        type=str,
        help="String. Name of the PyPSA-Earth config file used as template "
        "for the GUI.",
    )
    parser.add_argument(
        'default_visible',
        type=convert_to_bool,
        help="Boolean. Default value for the widget's visible attribute.",
    )
    parser.add_argument(
        'default_disabled',
        type=convert_to_bool,
        help="Boolean. Default value for the widget's disabled attribute.",
    )
    args = parser.parse_args()

    context = BuilderContext(
        args.config_file_name,
        Path(BASE_DIR, UI_CONFIG_METADATA_FILE_NAME),
        default_visible=args.default_visible,
        default_disabled=args.default_disabled,
    )

    with open(context.config_file_name, 'r') as config_template:
        config_data: dict = safe_load(config_template)
        context.ui_config_metadata = config_data.copy()
        for parameter_name, parameter_value in config_data.items():
            update_ui_config_metadata(
                context,
                Parameter(parameter_name, parameter_value),
                set(),
            )

    with open(context.ui_config_metadata_file_path, 'w') as output_file:
        dump(
            context.ui_config_metadata,
            output_file,
            default_flow_style=False,
            indent=2,
            sort_keys=False,
        )
        dump(
            _DEFAULT_METADATA,
            output_file,
            default_flow_style=False,
            indent=2,
        )

    logger.info(
        f"Number of parameters processed: {context.parameter_count}."
    )


if __name__ == '__main__':
    main()