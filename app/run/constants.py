"""App's run module constants.

Constants
---------
MSG_SELECT_FOLDER_FIRST \\
MSG_CREATE_CONFIG_FIRST \\
RUN_DIVIDER_COLOR \\
PYTHON_ENVS_SUBHEADER_LABEL \\
SNAKEMAKE_SUBHEADER_LABEL \\
EXECUTION_SUBHEADER_LABEL \\
TIMEOUT_LABEL \\
TIMEOUT_HELPER \\
RUN_BUTTON_LABEL \\
RUN_BUTTON_ICON \\
MSG_NO_ENV_MNGR_INSTALLED \\
MNGR_SELECTBOX_LABEL \\
ENV_SELECTBOX_LABEL \\
MSG_ERROR_ON_TRYING_TO_RUN_COMMAND \\
"""

from typing import Literal


###### RUN VIEW CONSTANTS ######
MSG_SELECT_FOLDER_FIRST = "Please select the PyPSA-Earth directory first."
MSG_CREATE_CONFIG_FIRST = "Please create a configuration first."
RUN_DIVIDER_COLOR: Literal['blue', 'green', 'orange', 'red', 'violet', 'yellow', 
                       'gray', 'grey', 'rainbow'] = 'blue'
PYTHON_ENVS_SUBHEADER_LABEL = "Python Environment"
SNAKEMAKE_SUBHEADER_LABEL = "Snakemake"
EXECUTION_SUBHEADER_LABEL = "Execution"
TIMEOUT_LABEL = "Timeout (m):"
TIMEOUT_HELPER = "In minutes. Set to 0 for no timeout (not recommended)."
RUN_BUTTON_LABEL = "Run"
RUN_BUTTON_ICON = ":material/play_circle:" 

###### ENVS COMMANDS CONSTANTS ######
MSG_NO_ENV_MNGR_INSTALLED = "No Python environment manager installed. Check " \
    + "your PyPSA-Earth installation."
MNGR_SELECTBOX_LABEL = "Manager:"
ENV_SELECTBOX_LABEL = "PyPSA-Earth Environment:"

###### PROCESS EXECUTION CONSTANTS ######
MSG_ERROR_ON_TRYING_TO_RUN_COMMAND = "Unexpected error on trying to run " \
    + "command. Try again or contact the PyPSA-Earth GUI support."

###### PROCESS MONITORING CONSTANTS ######
MINUTES_TO_SECONDS: Literal[60] = 60
MSG_ERROR_DURING_RUN = "Unexpected error when running PyPSA-Earth. " \
    + "Try again or contact the PyPSA-Earth GUI support."