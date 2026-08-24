"""App's configuration form widgets metadata retrieval functions.

Functions
---------
infer_widget_metadata_for(parameter: Parameter) -> dict[str, Any]
"""

from pathlib import Path
from re import search
from typing import Any

from app.config.parameters import Parameter
from app.helpers.logging import get_logger_named
from app.helpers.math import is_number
from app.helpers.ui.widgets import Metadata, WidgetType


logger = get_logger_named(Path(__file__).stem)


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
