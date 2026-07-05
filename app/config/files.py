"""App's configuration files.

Classes
-------
ConfigTemplateFiles() \\
ConfigFiles(ConfigTemplateFiles)
"""

from pathlib import Path

from app.config.constants import CONFIG_FILES_EXTENSION


class ConfigTemplateFiles():
    """Class that hosts a list of PyPSA-Earth's configuration template files.
    
    Entries:
        - DEFAULT: 'config.default.yaml'
        - TUTORIAL: 'config.tutorial.yaml'
    
    Methods
    -------
    to_list(cls) -> list[str]
    """

    DEFAULT = f'config.default.{CONFIG_FILES_EXTENSION}'
    TUTORIAL = f'config.tutorial.{CONFIG_FILES_EXTENSION}'

    @classmethod
    def to_list(cls) -> list[str]:
        """Get the configuration template file names.
        
        Returns
        -------
        list[str]
            A list of the available configuration template file names.
        """
        return [cls.DEFAULT, cls.TUTORIAL]


class ConfigFiles(ConfigTemplateFiles):
    """Class that hosts a list of all PyPSA-Earth's configuration files.
    
    It inherits from ConfigTemplateFiles.

    Entries:
        - DEFAULT: 'config.default.yaml'
        - TUTORIAL: 'config.tutorial.yaml'
        - CONFIG: 'config.yaml'
    
    Methods
    -------
    to_list(cls) -> list[str] \\
    get_unique_id(cls, config_file_path: Path) -> str
    """

    CONFIG = f'config.{CONFIG_FILES_EXTENSION}'

    @classmethod
    def to_list(cls) -> list[str]:
        """Get the configuration file names.
        
        Returns
        -------
        list[str]
            A list of the PyPSA-Earth configuration file names.
        """
        return super().to_list() + [cls.CONFIG]

    @classmethod
    def get_unique_id(cls, config_file_path: Path) -> str:
        """Get the unique id from the file name in config_file_path.
        
        The unique identifiers for each entry in ConfigFiles are:
        - config.yaml => config
        - config.default.yaml => default
        - config.tutorial.yaml => tutorial

        Parameters
        ----------
        config_file_path: Path
            The path to the configuration file used to extract the unique id.
        
        Returns
        -------
        str
            The string unique identifier of the configuration file.
        """
        match config_file_path.name:
            case cls.DEFAULT:
                return 'default'
            case cls.TUTORIAL:
                return 'tutorial'
            case cls.CONFIG:
                return 'config'