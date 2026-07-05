"""App's configuration constants.

Constants
---------
CONFIG_FILES_EXTENSION \\
ACTION_SELECT_LABEL \\
TEMPLATE_SELECT_LABEL \\
DISPLAY_CONFIG_FORM_ERROR_MSG \\
SAVE_BUTTON_LABEL \\
SAVE_BUTTON_HELP \\
UI_METADATA_DEFAULT_ID \\
UI_CONFIG_METADATA_FILE_NAME
"""

###### GENERAL CONFIG CONSTANTS ######
CONFIG_FILES_EXTENSION: str = 'yaml'

###### CONFIG VIEW CONSTANTS ######
ACTION_SELECT_LABEL: str = "Choose an action"
TEMPLATE_SELECT_LABEL: str = "Choose a template"
DISPLAY_CONFIG_FORM_ERROR_MSG: str = "Unexpected error; could not render " \
    + "app's GUI. Contact support."
SAVE_BUTTON_LABEL: str = "SAVE"
SAVE_BUTTON_HELP: str = "Click to persist data modifications to file."

###### CONFIG METADATA CONSTANTS ######
UI_METADATA_DEFAULT_ID: str = 'default'
UI_CONFIG_METADATA_FILE_NAME: str = \
    f'ui_config_metadata.{CONFIG_FILES_EXTENSION}'



