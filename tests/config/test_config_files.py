"""Tests for module app.config.files.py"""

from pathlib import Path

from app.config.files import ConfigFiles, ConfigTemplateFiles


def test_config_template_files(
        config_template_file_names: list[str],
    ) -> None:
    """"""
    assert ConfigTemplateFiles.to_list() == config_template_file_names


def test_config_files(
        config_file_name: str,
        config_template_file_names: list[str],
    ) -> None:
    """"""
    assert ConfigFiles.to_list() == \
        config_template_file_names + [config_file_name]
    
    assert ConfigFiles.get_unique_id(Path(config_file_name)) == 'config'
    assert ConfigFiles.get_unique_id(Path(config_template_file_names[0])) == \
        'default'
    assert ConfigFiles.get_unique_id(Path(config_template_file_names[1])) == \
        'tutorial'
    assert ConfigFiles.get_unique_id(Path("unknown.yaml")) == None