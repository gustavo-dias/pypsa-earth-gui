"""Tests for module validators.py"""

from pathlib import Path

from app.helpers.validators import is_pypsa_earth_folder_path


def test_is_pypsa_earth_folder_path(pypsa_earth_folder_path: Path) -> None:
    """"""
    assert is_pypsa_earth_folder_path(pypsa_earth_folder_path)