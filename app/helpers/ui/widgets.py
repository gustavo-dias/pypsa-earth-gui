"""App's UI widgets helpers.

Classes
-------
WidgetType() \\
Metadata()

Functions
---------
display_widget_for(parameter: Parameter) -> None
"""

from pathlib import Path

import streamlit as st

from app.config.parameters import Parameter
from app.config.callback import save_on_change
from app.helpers.data import load_data
from app.helpers.datetime import get_date_in_isoformat
from app.helpers.logging import get_logger_named
from app.helpers.math import convert_scientific_to_float


logger = get_logger_named(Path(__file__).stem)


class WidgetType():
    """Class that hosts a list of widget types.
    
    Entries:
        - CHECKBOX: 'checkbox'
        - NUMBER_INPUT: 'number_input'
        - COLOR_PICKER: 'color_picker'
        - MULTISELECT: 'multiselect'
        - DATE_INPUT: 'date_input'
        - TEXT_INPUT: 'text_input'
        - SELECTBOX: 'selectbox'
    """
    CHECKBOX: str = 'checkbox'
    NUMBER_INPUT: str = 'number_input'
    COLOR_PICKER: str = 'color_picker'
    MULTISELECT: str = 'multiselect'
    DATE_INPUT: str = 'date_input'
    TEXT_INPUT: str = 'text_input'
    SELECTBOX: str = 'selectbox'


class Metadata():
    """Class that hosts a list of widget metadata fields.
    
    Entries:
        - WIDGET_TYPE: 'type'
        - HELPER: 'helper'
        - VISIBLE: 'visible'
        - DISABLED: 'disabled'
        - WIDTH: 'width'
        - OPTIONS: 'options'
    """
    WIDGET_TYPE: str = 'type'
    HELPER: str = 'helper'
    VISIBLE: str = 'visible'
    DISABLED: str = 'disabled'
    WIDTH: str = 'width'
    OPTIONS: str = 'options'


def display_widget_for(parameter: Parameter) -> None:
    """Display a widget for parameter.
    
    Parameters
    ----------
    parameter: Parameter
        A PyPSA-Earth parameter object.
    
    Returns
    -------
    None
    """
    if parameter.widget_metadata[Metadata.VISIBLE]:
        disabled = parameter.widget_metadata.get(Metadata.DISABLED, False)
        helper = parameter.widget_metadata.get(Metadata.HELPER, None)
        width = parameter.widget_metadata.get(Metadata.WIDTH, 'stretch')
        parameter_widget_type = parameter.widget_metadata[Metadata.WIDGET_TYPE]
        callback_args = (parameter.unique_id,)
        try:
            match parameter_widget_type:
                case WidgetType.CHECKBOX:
                    st.checkbox(
                        label=parameter.name,
                        value=parameter.value,
                        key=parameter.unique_id,
                        disabled=disabled,
                        help=helper,
                        on_change=save_on_change,
                        args=callback_args,
                    )
                case WidgetType.NUMBER_INPUT:
                    st.number_input(
                        label=f"{parameter.label}:",
                        value=convert_scientific_to_float(parameter.value),
                        key=parameter.unique_id,
                        disabled=disabled,
                        help=helper,
                        width=width,
                        on_change=save_on_change,
                        args=callback_args,
                    )
                case WidgetType.COLOR_PICKER:
                    st.color_picker(
                        label=f"{parameter.label}:",
                        value=parameter.value,
                        key=parameter.unique_id,
                        disabled=disabled,
                        help=helper,
                        width=width,
                        on_change=save_on_change,
                        args=callback_args,
                    )
                case WidgetType.SELECTBOX:
                    options: list = load_data(
                        parameter.widget_metadata.get(Metadata.OPTIONS, [])
                    ) + parameter.value
                    if options == parameter.value:
                        accept_new = True
                    else:
                        accept_new = False
                    st.selectbox( # type: ignore
                        label=f"{parameter.label}:",
                        key=parameter.unique_id,
                        default=parameter.value,
                        disabled=disabled,
                        help=helper,
                        width=width,
                        options=options,
                        accept_new_options=accept_new,
                        on_change=save_on_change,
                        args=callback_args,
                    )
                case WidgetType.MULTISELECT:
                    options: list = load_data(
                        parameter.widget_metadata.get(Metadata.OPTIONS, [])
                    ) + parameter.value
                    if options == parameter.value:
                        accept_new = True
                    else:
                        accept_new = False
                    st.multiselect(
                        label=f"{parameter.label}:",
                        key=parameter.unique_id,
                        default=parameter.value,
                        options=options,
                        disabled=disabled,
                        help=helper,
                        width=width,
                        accept_new_options=accept_new,
                        on_change=save_on_change,
                        args=callback_args,
                    )
                case WidgetType.DATE_INPUT:
                    st.date_input(
                        label=f"{parameter.label}:",
                        value=get_date_in_isoformat(parameter.value),
                        key=parameter.unique_id,
                        disabled=disabled,
                        help=helper,
                        width=width,
                        on_change=save_on_change,
                        args=callback_args,
                    )
                case WidgetType.TEXT_INPUT:
                    st.text_input(
                        label=f"{parameter.label}:",
                        value=parameter.value,
                        key=parameter.unique_id,
                        disabled=disabled,
                        help=helper,
                        width=width,
                        on_change=save_on_change,
                        args=callback_args,
                    )
        except Exception as exc:
            logger.error(
                f"On displaying {parameter_widget_type} for parameter"
                f" {parameter.unique_id}: {exc}."
            )
        

