"""App's configuration form widgets metadata retrieval functions.

Functions
---------
get_widget_metadata_for(parameter: Parameter) -> dict
"""

from pathlib import Path

from app.config.constants import UI_METADATA_DEFAULT_ID
from app.config.parameters import Parameter
from app.helpers.exceptions import CriticalAppError
from app.helpers.logging import get_logger_named
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
