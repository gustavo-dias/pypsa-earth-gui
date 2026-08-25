"""Tests for the module gets.py"""

from app.session_state.constants import SS_IS_SOLVING_KEY
from app.session_state.gets import get_is_solving_from_ss
from app.session_state.constants import SS_FOLDER_PATH_KEY
from app.session_state.gets import get_folder_path_from_ss
from app.session_state.constants import SS_SAVE_BUTTON_DISABLED_KEY
from app.session_state.gets import get_save_button_disabled_from_ss

def test_get_folder_path_from_ss() -> None:
    """"""
    import streamlit as st
    from pathlib import Path

    assert get_folder_path_from_ss() == None, 'None (i.e. not set)'

    st.session_state[SS_FOLDER_PATH_KEY] = Path('/test/folder/path')

    assert get_folder_path_from_ss() == Path('/test/folder/path'), 'Path'

    del st.session_state[SS_FOLDER_PATH_KEY]


def test_get_save_button_disabled_from_ss() -> None:
    """"""
    import streamlit as st

    # not sure why, but whithout this delete, the function returns False, when
    # it should return True; it is as if the key is being initialized before
    # the assert; TODO: investigate
    del st.session_state[SS_SAVE_BUTTON_DISABLED_KEY]

    assert get_save_button_disabled_from_ss() == True, 'Default (True) failed'

    st.session_state[SS_SAVE_BUTTON_DISABLED_KEY] = False

    assert not get_save_button_disabled_from_ss(), 'False failed'

    del st.session_state[SS_SAVE_BUTTON_DISABLED_KEY]


def test_get_is_solving_from_ss() -> None:
    """"""
    import streamlit as st

    assert get_is_solving_from_ss() == False, "False failed"

    st.session_state[SS_IS_SOLVING_KEY] = True

    assert get_is_solving_from_ss() == True, "True failed"

    del st.session_state[SS_IS_SOLVING_KEY] # delete to not impact other tests
