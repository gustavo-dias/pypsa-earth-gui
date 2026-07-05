"""Tests for module navigation.py"""

from app.config.navigation import parameter_was_not_visited
from app.config.parameters import Parameter


def test_parameter_was_not_visited(parameter: Parameter) -> None:
    """"""
    visited_set = {Parameter('dummy_parameter', 1980)}
    assert parameter_was_not_visited(parameter, visited_set)

    visited_set.add(parameter)
    assert not parameter_was_not_visited(parameter, visited_set)
