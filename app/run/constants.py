"""App's run module constants.

Constants
---------
MSG_SELECT_FOLDER_FIRST \\
MSG_CREATE_CONFIG_FIRST \\
DIVIDER_COLOR \\
"""

from typing import Literal


###### RUN VIEW CONSTANTS ######
MSG_SELECT_FOLDER_FIRST = "Please select the PyPSA-Earth directory first."
MSG_CREATE_CONFIG_FIRST = "Please create a configuration first."
DIVIDER_COLOR: Literal['blue', 'green', 'orange', 'red', 'violet', 'yellow', 
                       'gray', 'grey', 'rainbow'] = 'blue'
PYTHON_ENVS_SUBHEADER_LABEL = "Python Environment"
SNAKEMAKE_SUBHEADER_LABEL = "Snakemake"
EXECUTION_SUBHEADER_LABEL = "Execution" 