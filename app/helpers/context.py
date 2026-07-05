"""App's context helpers.

Classes
-------
BuilderContext()
"""

class BuilderContext():
    """Class that represents UI config metadata builder contexts.
    
    A context contains relevant global data for the builder application. It is
    passed throughout function calls to provide relevant global data locally.
    """

    def __init__(
            self,
            config_file_name: str,
            ui_config_metadata_file_name: str,
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
        ui_config_metadata_file_name: str
            Name of the PyPSA-Earth App UI configuration file.
        parameter_count: int
            Count on the number of config_file_name parameters processed.
        ui_config_metadata: dict
            The actual metadata for the UI; content to be written to 
            ui_config_metadata_file_name.
        default_visible: bool
            Default value for the widget's visible attribute.
        defaut_disabled: bool
            Default value for the widget's disabled attribute.
        """
        self.config_file_name = config_file_name
        """Name of the PyPSA-Earth config file used as template for the UI."""
        self.ui_config_metadata_file_name = ui_config_metadata_file_name
        """Name of the PyPSA-Earth App UI configuration file."""
        self.parameter_count = parameter_count
        """Count on the number of config_file_name parameters processed."""
        self.ui_config_metadata = ui_config_metadata
        """The actual metadata for the UI; content to be written to
        ui_config_metadata_file_name.
        """
        self.default_disabled = default_disabled
        """Default value for the widget's visible attribute."""
        self.default_visible = default_visible
        """Default value for the widget's disabled attribute."""
        self.helper_line_idx = -1
        """Pointer used to parse the config file and retrieve parameters' 
        helpers.
        """