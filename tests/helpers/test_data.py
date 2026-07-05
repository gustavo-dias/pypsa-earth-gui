"""Tests for module data.py"""

from pathlib import Path

from app.helpers.data import load_data


def test_load_data(
        file_path: Path,
        code_column: str,
        country_codes: list[str],
    ) -> None:
    """"""
    # country code data
    assert load_data((file_path, code_column)) == country_codes
        