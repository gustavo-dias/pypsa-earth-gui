"""App's session state 'private' constants.

Not recommended to make any runtime changes to these constants risking critical
errors.

Constants
---------
_SS_FOLDER_PATH_KEY \\
_SS_SAVE_BUTTON_DISABLED_KEY \\
_SS_UI_CONFIG_METADATA_KEY \\
_SS_CONFIG_DATA_KEY \\
_SS_UNSAVED_CHANGES_KEY
"""

_SS_FOLDER_PATH_KEY: str = "folder_path"
_SS_SAVE_BUTTON_DISABLED_KEY: str = 'save_disabled'
_SS_UI_CONFIG_METADATA_KEY: str = 'ui_config_metadata'
_SS_CONFIG_DATA_KEY: str = 'config_data'
_SS_UNSAVED_CHANGES_KEY: str = 'unsaved_changes'