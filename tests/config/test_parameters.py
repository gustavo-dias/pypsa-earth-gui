"""Tests for module parameters.py"""

from pytest import raises

from app.config.parameters import Parameter


def test_parameter(
        parameter_name: str,
        parameter_value: int,
        parameter_unique_id_prefix: str,
        parameter_ancestors: list[str],
    ) -> None:
    """"""
    # missing two required arguments
    with raises(TypeError):
        Parameter()
    # missing one required argument
    with raises(TypeError):
        Parameter(parameter_name)

    # parameter default creation
    p = Parameter(parameter_name, parameter_value)
    assert p.name == parameter_name
    assert p.value == parameter_value
    assert p.unique_id_prefix == p._default_unique_id_prefix
    assert p.hierarchy == [parameter_name]
    assert p.widget_metadata == {}

    # parameter non-default creation
    p = Parameter(
        parameter_name,
        parameter_value,
        parameter_unique_id_prefix,
        parameter_ancestors,
    )
    assert p.name == parameter_name
    assert p.value == parameter_value
    assert p.unique_id_prefix == parameter_unique_id_prefix
    assert p.hierarchy == parameter_ancestors + [parameter_name]
    assert p.widget_metadata == {}

    # label is name capitalized
    assert p.label == parameter_name.capitalize()

    # widget metadata must be a dict
    with raises(TypeError):
        p.widget_metadata = 'string'

    # parameter's string representation
    assert str(p) == f'{parameter_name}: {parameter_value}'

    # parameter's unique id
    assert p.unique_id == \
        f'{parameter_unique_id_prefix}{p._unique_id_delimiter}' + \
        f'{parameter_ancestors[0]}{p._unique_id_delimiter}' + \
        f'{parameter_ancestors[1]}{p._unique_id_delimiter}{parameter_name}'
    
    # setters
    p.name = 'new_name'
    assert p.name == 'new_name'
    p.value = -6.6
    assert p.value == -6.6
    p.widget_metadata = {'type': 'checkbox'}
    assert p.widget_metadata == {'type': 'checkbox'}

    # methods
    p.remove_from_hierarchy(0)
    assert p.hierarchy == [parameter_ancestors[1], parameter_name]

    p = Parameter.get_parameter_from_unique_id(
        f'{parameter_unique_id_prefix}{p._unique_id_delimiter}'
        f'{parameter_ancestors[0]}{p._unique_id_delimiter}{parameter_name}',
        2026,
    )
    assert p.name == parameter_name
    assert p.value == 2026
    assert p.unique_id_prefix == parameter_unique_id_prefix
    assert p.hierarchy == [parameter_ancestors[0], parameter_name]