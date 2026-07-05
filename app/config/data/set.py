"""App's configuration data set functions.

Functions
---------
set_config_data(config_data: dict, parameter: Parameter) -> None:
"""

from app.config.parameters import Parameter
from app.session_state.sets import set_save_button_disabled_in_ss
from app.session_state.sets import set_unsaved_changes_in_ss


def set_config_data(config_data: dict, parameter: Parameter) -> None:
    """Update the parameter's value in config_data.
    
    The function recursively calls itself to navigate into higher levels of the
    config_data structure following the parameter's hierarchy. Levels:

    param0:                 <- level 0
        param1:             <- level 1
            param2:         <- level 2 \\
                . . .
                    paramN  <- level N

    Parameters
    ----------
    config_data: dict
        The complete config_data dictionary.
    parameter: Parameter
        A PyPSA-Earth parameter object.
    
    Returns
    -------
    None
    """
    if len(parameter.hierarchy) == 1:
        config_data[parameter.name] = parameter.value
        set_unsaved_changes_in_ss(True)
        set_save_button_disabled_in_ss(False)
    else:
        # to navigate into higher levels, pass to set_config_data the 
        # config_data associated with the lowest level entry (idx=0)
        # in parameter's hierarchy whilst also removing it from the hierarchy
        current_hierarchy_idx: int = 0
        current_key = parameter.hierarchy[current_hierarchy_idx]
        parameter.remove_from_hierarchy(current_hierarchy_idx)
        set_config_data(
            config_data[current_key],
            parameter,
        )
