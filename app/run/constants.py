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
MINUTES_TO_SECONDS \\
MSG_ERROR_DURING_RUN \\
DRYRUN_CHECKBOX_LABEL \\
CORES_INPUT_LABEL \\
CORES_INPUT_HELPER \\
EXTRA_ARGS_LABEL \\
EXTRA_ARGS_HELPER \\
RULES_SELECTBOX_LABEL \\
RULES_SELECTBOX_HELPER \\
COMMAND_INPUT_LABEL \\
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

###### SNAKEMAKE COMMANDS CONSTANTS ######
DRYRUN_CHECKBOX_LABEL = "Dry run?"
CORES_INPUT_LABEL = "Number of cores:"
CORES_INPUT_HELPER = "Range: [1, local CPU count]"
EXTRA_ARGS_LABEL = "Extra arguments:"
EXTRA_ARGS_HELPER = 'E.g.: "--rerun-incomplete"'
RULES_SELECTBOX_LABEL = "PyPSA-Earth rules:"
RULES_SELECTBOX_HELPER = "Choose (or type to add) a rule."
COMMAND_INPUT_LABEL = "Command:"