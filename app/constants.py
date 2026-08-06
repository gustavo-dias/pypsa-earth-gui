"""App's main constants.

Constants
---------
BASE_DIR \\
LOGO_PATH \\
LOGO_LINK_URL \\
LOGO_SIZE \\
HEADER_DIVIDER \\
WORKING_DIR \\
FOLDER_BUTTON_LABEL \\
FOLDER_PROMPT_TITLE \\
ERROR_MSG
"""

from typing import Literal

from app.config.constants import CONFIG_FILES_EXTENSION

###### GENERAL ######
BASE_DIR: str = 'app'
LOGO_PATH: str = f'./{BASE_DIR}/static/logo.png'
LOGO_LINK_URL: str = 'https://pypsa-meets-earth.github.io/'
LOGO_SIZE: Literal['small', 'medium', 'large'] = 'large'

###### ENTRY VIEW CONSTANTS ######
HEADER_DIVIDER: str = 'blue' # https://docs.streamlit.io/develop/api-reference/text/st.header
WORKING_DIR: str = "Working directory:"
FOLDER_BUTTON_LABEL: str = "Select PyPSA-Earth Directory"
FOLDER_PROMPT_TITLE: str = FOLDER_BUTTON_LABEL
ERROR_MSG: str = f"PyPSA-Earth {CONFIG_FILES_EXTENSION} files not present " \
    + "in the selected directory. You can: \n - Select another folder " \
    + "or; \n - Check your PyPSA-Earth (local) installation."