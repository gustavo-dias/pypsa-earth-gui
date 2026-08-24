"""Tests for the module sets.py"""

from app.session_state.constants import SS_IS_SOLVING_KEY
from app.session_state.sets import set_is_solving_in_ss
from app.session_state.constants import SS_FOLDER_PATH_KEY
from app.session_state.sets import set_folder_path_in_ss


def test_set_folder_path_in_ss() -> None:
    """"""
    import streamlit as st
    from pathlib import Path

    set_folder_path_in_ss(None)
    assert st.session_state[SS_FOLDER_PATH_KEY] is None, 'None'

    path = Path('/test/folder/path')
    set_folder_path_in_ss(path)

    assert st.session_state[SS_FOLDER_PATH_KEY] == path, 'Path'

    del st.session_state[SS_FOLDER_PATH_KEY]


def test_set_is_solving_in_ss() -> None:
    """"""
    import streamlit as st

    set_is_solving_in_ss(True)
    assert st.session_state[SS_IS_SOLVING_KEY] == True, "True failed"

    set_is_solving_in_ss(False)
    assert st.session_state[SS_IS_SOLVING_KEY] == False, "False failed"

    del st.session_state[SS_IS_SOLVING_KEY] # delete to not impact other tests