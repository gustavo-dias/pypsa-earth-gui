"""Tests for module validators.py"""

from os import listdir
from pathlib import Path

from app.helpers.validators import is_pypsa_earth_folder_path
from app.helpers.validators import is_there_a_config_yaml_in


def test_is_pypsa_earth_folder_path(pypsa_earth_folder_path: Path) -> None:
    """"""
    assert is_pypsa_earth_folder_path(pypsa_earth_folder_path)


def test_is_there_a_config_yaml_in(pypsa_earth_folder_path: Path) -> None:
    """"""
    files: list[str] = listdir(pypsa_earth_folder_path)
    # the fixture pypsa_earth_folder_path randomly decides whether or not to 
    # include the config.yaml in the path, so we need to check how many files
    # are there first before asserting
    if len(files) == 3: # all three yaml files
        assert is_there_a_config_yaml_in(pypsa_earth_folder_path), "true"
    else: # == 2; only two yaml files (config.yaml not included)
        assert not is_there_a_config_yaml_in(pypsa_earth_folder_path), "false"