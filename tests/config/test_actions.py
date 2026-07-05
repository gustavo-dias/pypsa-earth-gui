"""Tests for module actions.py"""

from pathlib import Path

from app.config.actions import ConfigActions
from app.config.actions import get_available_configuration_actions


def test_config_actions() -> None:
    """"""
    assert ConfigActions.to_list() == \
        [ConfigActions.CREATE, ConfigActions.USE_EXISTING]

def test_get_available_configuration_actions(
        pypsa_earth_folder_path: Path,
    ) -> None:
    """"""
    actions = get_available_configuration_actions(pypsa_earth_folder_path)
    assert (actions == ConfigActions.to_list() or 
            actions == [ConfigActions.CREATE]) 