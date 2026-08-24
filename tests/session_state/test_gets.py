"""Tests for the module gets.py"""

from app.session_state.constants import SS_IS_SOLVING_KEY
from app.session_state.gets import get_is_solving_from_ss
from app.session_state.constants import SS_FOLDER_PATH_KEY
from app.session_state.gets import get_folder_path_from_ss


def test_get_folder_path_from_ss() -> None:
    """"""
    import streamlit as st
    from pathlib import Path

    assert get_folder_path_from_ss() == None, 'None (i.e. not set)'

    st.session_state[SS_FOLDER_PATH_KEY] = Path('/test/folder/path')

    assert get_folder_path_from_ss() == Path('/test/folder/path'), 'Path'

    del st.session_state[SS_FOLDER_PATH_KEY]


def test_get_is_solving_from_ss() -> None:
    """"""
    import streamlit as st

    assert get_is_solving_from_ss() == False, "False failed"

    st.session_state[SS_IS_SOLVING_KEY] = True

    assert get_is_solving_from_ss() == True, "True failed"

    del st.session_state[SS_IS_SOLVING_KEY] # delete to not impact other tests
