"""App's configuration view entry.

Functions
---------
main() -> None
"""

import streamlit as st

from pathlib import Path

from app.config.constants import SAVE_BUTTON_HELP, SAVE_BUTTON_LABEL
from app.config.constants import ACTION_SELECT_LABEL, TEMPLATE_SELECT_LABEL
from app.config.constants import DISPLAY_CONFIG_FORM_ERROR_MSG
from app.config.actions import ConfigActions
from app.config.actions import get_available_configuration_actions
from app.config.data.save import save_to_file
from app.config.files import ConfigFiles, ConfigTemplateFiles
from app.config.form.display import display_config_form_based_on
from app.helpers.logging import get_logger_named
from app.helpers.ui.messages import display_as_error
from app.helpers.exceptions import CriticalAppError
from app.session_state.gets import get_folder_path_from_ss
from app.session_state.gets import get_save_button_disabled_from_ss
from app.session_state.sets import set_unsavedchanges_and_savebutton_in_ss
from app.session_state.sets import set_save_button_disabled_in_ss
from app.session_state.sets import set_ui_config_metadata_in_ss
from app.session_state.sets import set_unsaved_changes_in_ss


logger = get_logger_named(Path(__file__).stem)


def main() -> None:
    """Entry point for the configuration view.
    
    Returns
    -------
    None
    """
    pypsa_earth_folder_path = get_folder_path_from_ss()
    if pypsa_earth_folder_path:
        # 1) first we prompt the user whether s/he wants to create a new
        # configuration from scratch or use an existing one (if available).
        try:
            selected_action: str = st.sidebar.selectbox(
                label=ACTION_SELECT_LABEL,
                index=None,
                options=get_available_configuration_actions(
                    pypsa_earth_folder_path
                ),
                placeholder=None,
                label_visibility='collapsed',
                key='selectbox_config_action',
                on_change=set_unsavedchanges_and_savebutton_in_ss,
            )
        except CriticalAppError as cae:
            display_as_error(str(cae))
        else:
            # 2) we decide which config file to be used as reference to render 
            # the config form
            selected_config_file: str = ''

            match selected_action:
                case ConfigActions.CREATE:
                    selected_config_file = st.sidebar.selectbox(
                        label=TEMPLATE_SELECT_LABEL,
                        index=None,
                        options=ConfigTemplateFiles.to_list(),
                        placeholder=TEMPLATE_SELECT_LABEL,
                        label_visibility='collapsed',
                        key='selectbox_config_template',
                        on_change=set_unsavedchanges_and_savebutton_in_ss,
                    )
                case ConfigActions.USE_EXISTING:
                    selected_config_file = ConfigFiles.CONFIG
                case _:
                    # do nothing in case of unsupported action
                    pass

            # 3) third we display the configuration form accordingly
            try:
                    config_file_path = Path(
                        pypsa_earth_folder_path,
                        selected_config_file,
                    )
            except TypeError:
                # Path raises TypeError in case selected_config_file is 
                # NoneType, which is the case when the user has not selected
                # a template file yet; no action needed, just pass
                pass
            else:
                try:
                    # calling set before every display attempt to update the ui
                    # metadata in the app's session state should the ui config
                    # metadata file be modified while streamlit is running
                    set_ui_config_metadata_in_ss()
                    if display_config_form_based_on(config_file_path):
                        if st.sidebar.button(
                            SAVE_BUTTON_LABEL,
                            width='stretch',
                            disabled=get_save_button_disabled_from_ss(),
                            help=SAVE_BUTTON_HELP,
                            on_click=set_save_button_disabled_in_ss,
                        ):
                            save_to_file(
                                Path(
                                    pypsa_earth_folder_path,
                                    ConfigFiles.CONFIG,
                                )
                            )
                            # set unsaved to false after dumping to file
                            # otherwise (e.g. using the on_click event of the
                            # save button) it causes the reloading of the
                            # original config file data into the app's session
                            # state in function display_config_form_based_on(),
                            # causing data loss
                            set_unsaved_changes_in_ss(False)
                except Exception as exc:
                    logger.error(exc)
                    display_as_error(DISPLAY_CONFIG_FORM_ERROR_MSG)


if __name__ == '__main__':
    main()