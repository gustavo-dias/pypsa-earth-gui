"""App's configuration form widgets metadata retrieval functions.

Functions
---------
get_widget_metadata_for(parameter: Parameter) -> dict
infer_widget_metadata_for(parameter: Parameter) -> dict[str, Any]
"""

from pathlib import Path
from re import search
from typing import Any

from app.config.constants import UI_METADATA_DEFAULT_ID
from app.config.parameters import Parameter
from app.helpers.exceptions import CriticalAppError
from app.helpers.logging import get_logger_named
from app.helpers.math import is_number
from app.helpers.ui.widgets import Metadata, WidgetType
from app.session_state.gets import get_ui_config_metadata_from_ss


logger = get_logger_named(Path(__file__).stem)


def get_widget_metadata_for(parameter: Parameter) -> dict:
    """Get the UI widget metadata for parameter.
    
    The UI metadata is recovered from the app's session state. Make sure the
    metadata is loaded there prior to invoking this function (see module 
    app.session_state.sets for more info) or CriticalAppError is raised. 

    Returns the metadata associated with UI_METADATA_DEFAULT_ID if: \\
    (a) specific metadata is not found for parameter or; \\
    (b) an error occurs during the search procedure.

    Parameters
    ----------
    parameter: Parameter
        A PyPSA-Earth parameter object.
    
    Returns
    -------
    dict
        A dictionary with the parameter's UI widget metadata.

    Raises
    ------
    CriticalAppError:
        If the UI config metadata is not found at the app's session state.
    """
    try:
        ui_metadata: dict = get_ui_config_metadata_from_ss()
    except KeyError:
        raise CriticalAppError(
            "get_widget_metadata_for(): ui config metadata not found in the "
            f"app's session state."
        )

    # in case metadata is not found for a particular parameter (i.e. a KeyError
    # exception is raised when accessing the dict ui_metadata), return the
    # default
    try:
        # start parsing the ui_metadata from the root parameter (i.e. the root
        # ancestor) in the parameter's hierarchy (i.e. index 0)
        hierarchy_idx: int = 0
        current_metadata: dict = ui_metadata[
            parameter.hierarchy[hierarchy_idx]
        ]
        while hierarchy_idx < len(parameter.hierarchy)-1:
            hierarchy_idx += 1
            current_metadata = current_metadata[
                parameter.hierarchy[hierarchy_idx]
            ]
        return current_metadata
    except KeyError:
        logger.warning(
            "Returning default ui metadata for parameter "
            f"{parameter.unique_id}."
        )
        return ui_metadata[UI_METADATA_DEFAULT_ID]
    except Exception as exc:
        logger.error(f"Unexpected exception '{exc}'.")
        logger.warning(
            "Returning default ui metadata for parameter "
            f"{parameter.unique_id}."
        )
        return ui_metadata[UI_METADATA_DEFAULT_ID]


def infer_widget_metadata_for(parameter: Parameter) -> dict[str, Any]:
    """Infer the UI widget metadata for parameter.

    It tries to identify the parameter's value type (str, number, list, etc) to
    return an appropriate widget metadata. Returns WidgetType.TEXT_INPUT by
    default in case the type is not identified.

    Parameters
    ----------
    parameter: Parameter
        The PyPSA-Earth's parameter to have the ui widget metadata retrieved.
    
    Returns
    -------
    dict[str, Any]
        A dictionary containing the parameter's UI widget metadata.
    """
    metadata: dict[str, Any] = {
        Metadata.DISABLED: False,
        Metadata.VISIBLE: True,
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
        metadata[Metadata.WIDGET_TYPE] = WidgetType.MULTISELECT
    # check for dates with format YYYY-MM-DD
    elif search(r'\d{2,4}-\d{1,2}-\d{1,2}', str(parameter.value)):
        metadata[Metadata.WIDGET_TYPE] = WidgetType.DATE_INPUT
    # check for strings; str must be the last case or many values (that
    # match the cases above) will also evaluate to str
    elif isinstance(parameter.value, str): 
        metadata[Metadata.WIDGET_TYPE] = WidgetType.TEXT_INPUT
    # and finally, everything else is treated as text input
    else:
        logger.warning(
            f"Returning default text_input to {parameter.name}: "
            f"{parameter.value}"
        )
        metadata[Metadata.WIDGET_TYPE] = WidgetType.TEXT_INPUT
    
    return metadata
