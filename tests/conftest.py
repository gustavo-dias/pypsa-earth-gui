"""Fixtures for pytests of PyPSA-Earth's app."""

import pytest

from random import randint
from pandas import read_csv
from pathlib import Path
from pytest_mock import MockerFixture

from app.config.parameters import Parameter


@pytest.fixture
def file_path() -> Path:
    """Fixture: get the country code file path."""
    return Path('./tests/helpers/data/test_country_codes.csv')

@pytest.fixture
def code_column() -> str:
    """Fixture: get name of code column in country iso code data file.""" 
    return 'Code'

@pytest.fixture
def country_codes(file_path: Path, code_column: str) -> list[str]:
    """Fixture: get list of country iso codes."""
    return read_csv(file_path)[code_column].to_list()

@pytest.fixture
def csv_file_extension() -> str:
    """Fixture: get the csv file extension."""
    return '.csv'

@pytest.fixture
def pypsa_earth_folder_path(tmp_path: Path, config_file_name: str) -> Path:
    """Fixture: get a valid PyPSA-Earth folder path."""
    pypsa_folder_path = tmp_path / 'configs'
    pypsa_folder_path.mkdir()
    default = pypsa_folder_path / 'config.default.yaml'
    default.write_text('default', encoding='utf-8')
    tutorial = pypsa_folder_path / 'config.tutorial.yaml'
    tutorial.write_text('text', encoding='utf-8')
    # by definition, a valid pypsa-earth folder must contain both yaml files
    # above while the config.yaml file is optional; randomly deciding at each
    # fixture call whether to include it or not
    if randint(0,1):
        config = pypsa_folder_path / config_file_name
        config.write_text('config', encoding='utf-8')
    return pypsa_folder_path

@pytest.fixture
def config_file_name() -> str:
    """Fixture: get the PyPSA-Earth configuration file name."""
    return 'config.yaml'

@pytest.fixture
def config_template_file_names() -> list[str]:
    """Fixture: get the PyPSA-Earth configuration template file names.
    
    Returns
    -------
    list[str]
        The list ['config.default.yaml', 'config.tutorial.yaml'].
    """
    return ['config.default.yaml', 'config.tutorial.yaml']


@pytest.fixture
def ui_config_metadata_file_name() -> str:
    """Fixture: get the PyPSA-Earth's app UI config metadata file name."""
    return 'ui_config_metadata.yaml'

@pytest.fixture
def parameter_name() -> str:
    """Fixture: get the parameter's name."""
    return 'param_2'

@pytest.fixture
def parameter_value() -> float:
    """Fixture: get the parameter's value."""
    return 6.6

@pytest.fixture
def parameter_unique_id_prefix() -> str:
    """Fixture: get the parameter's unique identifier prefix."""
    return 'unique_id_prefix'

@pytest.fixture
def parameter_ancestors() -> list[str]:
    """Fixture: get the parameter's ancestors."""
    return ['param_0', 'param_1']

@pytest.fixture
def parameter(
    parameter_name: str,
    parameter_value: int,
    parameter_unique_id_prefix: str,
    parameter_ancestors: list[str],
    ) -> Parameter:
    """Fixture: a PyPSA-Earth configuration parameter."""
    return Parameter(
        parameter_name,
        parameter_value,
        parameter_unique_id_prefix,
        parameter_ancestors,
    )
    
@pytest.fixture
def parameter_widget_metadata() -> dict:
    """Fixture: get parameter UI configuration metadata."""
    return {
        'type': 'checkbox',
        'helper': 'This is a checkbox',
        'visible': True,
        'disabled': False,
    }

@pytest.fixture
def snakemake_file(mocker: MockerFixture) -> None:
    """Fixture: mock a snakemake file with solve rules."""
    snakemake_file_data = mocker.mock_open( # type: ignore
        read_data="rule solve_all:\nrule solve_some:\nrule _solve_all:"
    )
    mocker.patch("builtins.open", snakemake_file_data)