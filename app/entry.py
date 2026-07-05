# Author: Gustavo Dias
# E-mail: gustavodias.po@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

"""PyPSA-Earth app's entry module.

Functions
---------
main() -> None
"""

import streamlit as st

from pathlib import Path

from app.helpers.ui.selectors import folder_selector
from app.helpers.validators import is_pypsa_earth_folder_path
from app.helpers.ui.messages import display_as_error
from app.constants import ERROR_MSG, HEADER_DIVIDER, FOLDER_BUTTON_LABEL
from app.constants import LOGO_LINK_URL, LOGO_PATH, LOGO_SIZE
from app.constants import FOLDER_PROMPT_TITLE, WORKING_DIR
from app.session_state.gets import get_folder_path_from_ss
from app.session_state.sets import set_folder_path_in_ss


def main() -> None:
    """Entry point for the PyPSA-Earth application.
    
    Returns
    -------
    None
    """
    st.logo(LOGO_PATH, size=LOGO_SIZE, link=LOGO_LINK_URL)

    st.set_page_config(layout='wide')

    st.header("PyPSA-Earth", divider=HEADER_DIVIDER)

    page = st.navigation(
        [
            st.Page(
                Path(Path(__file__).parent, 'home', 'home_view.py'),
                title="HOME",
            ),
            st.Page(
                Path(Path(__file__).parent, 'config', 'config_view.py'),
                title="CONFIG",
            ),
            st.Page(
                Path(Path(__file__).parent, 'solve', 'solve_view.py'),
                title="SOLVE",
            ),
            st.Page(
                Path(Path(__file__).parent, 'visualize', 'visualize_view.py'),
                title="VISUALIZE",
            )
        ],
        position='sidebar',
    )

    selected_folder_path: Path = get_folder_path_from_ss()

    folder_select_button = st.sidebar.button(
        FOLDER_BUTTON_LABEL,
        use_container_width=True,
        type='secondary',
        icon=":material/folder:",
    )
    if folder_select_button:
        selected_folder_path = folder_selector(
            title=FOLDER_PROMPT_TITLE,
        )
        # saving into session state to avoid reprompting user
        set_folder_path_in_ss(selected_folder_path) 
    if selected_folder_path:
        if is_pypsa_earth_folder_path(selected_folder_path):
            st.sidebar.write(f"{WORKING_DIR} {selected_folder_path}")
            st.sidebar.divider()
            page.run()
        else:
            # remove the invalid folder path from session state (set to None) 
            # to rerun the page and erase the error message once the user
            # navigates to another page or attempts to select other folder
            set_folder_path_in_ss(None)
            display_as_error(ERROR_MSG)
    else:
        page.run()


if __name__ == '__main__':
    main()