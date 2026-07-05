"""Tests for module app.helpers.files.py"""

from pathlib import Path

from app.helpers.files import get_files_of_type_in


def test_get_files_of_type_in(
        csv_file_extension: str,
        file_path: Path,
    ) -> None:
    """"""
    assert get_files_of_type_in(csv_file_extension, file_path.parent) == \
        [file_path.name]
    assert get_files_of_type_in(csv_file_extension, file_path.parent) != \
        ['file_path.name']