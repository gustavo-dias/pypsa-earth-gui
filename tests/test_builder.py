"""Tests for the module ui_config_metadata_builder.py"""

from pathlib import Path

from pytest import raises
from app.config.parameters import Parameter
from ui_config_metadata_builder import BuilderContext, convert_to_bool
from ui_config_metadata_builder import set_ui_config_metadata


def test_builder_context(
        config_file_name: str,
        ui_config_metadata_file_name: str,
    ) -> None:
    """"""
    # missing both required arguments
    with raises(TypeError):
        BuilderContext() # type: ignore
    
    # missing second required argument
    with raises(TypeError):
        BuilderContext(config_file_name) # type: ignore

    # builder default creation
    bc = BuilderContext(
        config_file_name,
        Path(ui_config_metadata_file_name),
    )
    assert bc.config_file_name == config_file_name
    assert bc.ui_config_metadata_file_path == \
        Path(ui_config_metadata_file_name)
    assert bc.parameter_count == 0
    assert bc.ui_config_metadata == {}
    assert bc.default_visible
    assert not bc.default_disabled
    assert bc.helper_line_idx == -1

    # builder non default creation
    bc = BuilderContext(
        config_file_name,
        Path(ui_config_metadata_file_name),
        6,
        {'tutorial': {'type': 'checkbox'}},
        False,
        True,
    )
    assert bc.config_file_name == config_file_name
    assert bc.ui_config_metadata_file_path == \
        Path(ui_config_metadata_file_name)
    assert bc.parameter_count == 6
    assert bc.ui_config_metadata == {'tutorial': {'type': 'checkbox'}}
    assert not bc.default_visible
    assert bc.default_disabled
    assert bc.helper_line_idx == -1


def test_convert_to_bool() -> None:
    """"""
    # successful conversions
    assert convert_to_bool('False') == False
    assert convert_to_bool('True') == True
    assert convert_to_bool(0) == False
    assert convert_to_bool(1) == True

    # unsuccessful conversions
    assert convert_to_bool(6) not in (True, False)
    assert convert_to_bool(6.6) not in (True, False)
    assert convert_to_bool('0') not in (True, False)
    assert convert_to_bool('1') not in (True, False)
    assert convert_to_bool('string') not in (True, False)


def test_set_ui_config_metadata(
        parameter: Parameter,
        parameter_widget_metadata: dict,
    ) -> None:
    """"""
    # parameter with no ancestors
    ui_config_metadata: dict = {}

    p = Parameter(parameter.name, parameter.value)
    p.widget_metadata = parameter_widget_metadata

    set_ui_config_metadata(ui_config_metadata, p)

    assert ui_config_metadata == {parameter.name: parameter_widget_metadata}

    # parameter with ancestors
    ui_config_metadata = {
        parameter.hierarchy[0]: {
            parameter.hierarchy[1]: {
                parameter.name: None
            }
        }
    }
    edited_ui_config_metadata = {
        parameter.hierarchy[0]: {
            parameter.hierarchy[1]: {
                parameter.name: parameter_widget_metadata
            }
        }
    }
    parameter.widget_metadata = parameter_widget_metadata

    set_ui_config_metadata(ui_config_metadata, parameter)

    assert ui_config_metadata == edited_ui_config_metadata


