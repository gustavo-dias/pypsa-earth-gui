"""App's configuration navigation.

Functions
---------
parameter_was_not_visited(parameter: Parameter, visited_set: set[Parameter]) -> bool
"""

from app.config.parameters import Parameter


def parameter_was_not_visited(
        parameter: Parameter,
        visited_set: set[Parameter],
    ) -> bool:
    """Return True if parameter is not in visited_set; False otherwise.
    
    The test is performed using parameter.unique_id (and not parameter.name)
    since parameters' names are not necessarily unique in PyPSA-Earth's config
    file.

    Parameters
    ----------
    parameter: Parameter
        The parameter to be tested.
    visited_set: set[Parameter]
        The set of visited parameters.
    
    Returns
    -------
    bool
        Whether or not the parameter has already been visited.
    """
    for visited_parameter in visited_set:
        if parameter.unique_id == visited_parameter.unique_id:
            return False
    return True
