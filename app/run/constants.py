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