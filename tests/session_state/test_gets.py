"""Tests for the module gets.py"""

from app.session_state.gets import SS_IS_SOLVING_KEY
from app.session_state.gets import get_is_solving_from_ss


def test_get_is_solving_from_ss() -> None:
    """"""
    import streamlit as st

    assert get_is_solving_from_ss() == False, "False failed"

    st.session_state[SS_IS_SOLVING_KEY] = True

    assert get_is_solving_from_ss() == True, "True failed"

    del st.session_state[SS_IS_SOLVING_KEY] # delete to not impact other tests
