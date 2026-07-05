"""Tests for module set.py"""

from app.config.data.set import set_config_data
from app.config.parameters import Parameter


def test_set_config_data(
        parameter_name: str,
        parameter_value: int,
        parameter_unique_id_prefix: str,
        parameter_ancestors: list[str]
    ) -> None:
    """"""
    # parameter with no ancestors
    config_data: dict = {}
    p = Parameter(parameter_name, parameter_value)

    set_config_data(config_data, p)

    assert config_data == {parameter_name: parameter_value}

    # parameter with ancestors
    config_data = {
        parameter_ancestors[0]: {
            parameter_ancestors[1]: {
                parameter_name: -1980
            }
        }
    }
    edited_config_data = {
        parameter_ancestors[0]: {
            parameter_ancestors[1]: {
                parameter_name: parameter_value
            }
        }
    }
    set_config_data(
        config_data,
        Parameter(
            parameter_name,
            parameter_value,
            parameter_unique_id_prefix,
            parameter_ancestors,
        ),
    )
    assert config_data == edited_config_data