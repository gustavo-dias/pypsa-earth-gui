"""App's session state 'private' constants.

Not recommended to make any runtime changes to these constants risking critical
errors.

Constants
---------
SS_FOLDER_PATH_KEY \\
SS_SAVE_BUTTON_DISABLED_KEY \\
SS_UI_CONFIG_METADATA_KEY \\
SS_CONFIG_DATA_KEY \\
SS_UNSAVED_CHANGES_KEY \\
SS_IS_SOLVING \\
"""

from typing import Literal


SS_FOLDER_PATH_KEY: Literal['folder_path'] = 'folder_path'
SS_SAVE_BUTTON_DISABLED_KEY: Literal['save_disabled'] = 'save_disabled'
SS_UI_CONFIG_METADATA_KEY: Literal['ui_config_metadata']= 'ui_config_metadata'
SS_CONFIG_DATA_KEY: Literal['config_data'] = 'config_data'
SS_UNSAVED_CHANGES_KEY: Literal['unsaved_changes'] = 'unsaved_changes'
SS_IS_SOLVING_KEY: Literal['is_solving'] = 'is_solving'