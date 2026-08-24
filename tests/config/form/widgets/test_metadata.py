"""Tests for module metadata.py"""

import numpy as np

from app.config.form.widgets.metadata import infer_widget_metadata_for
from app.config.parameters import Parameter
from app.helpers.ui.widgets import Metadata, WidgetType


def test_infer_widget_metadata_for() -> None:
    """"""
    param = Parameter('parameter', None)

    # boolean type
    param.value = True
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.CHECKBOX, 'boolean failed'

    # number type
    param.value = 1.0
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.NUMBER_INPUT, 'number failed'

    # color type
    param.value = '#FFFFFF'
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.COLOR_PICKER, 'color failed'

    # list type
    param.value = ['NG', 'BJ']
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.MULTISELECT, 'list failed'

    # date type
    param.value = '2026-08-24'
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.DATE_INPUT, 'date failed'

    # text type
    param.value = 'Lorem ipsum'
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.TEXT_INPUT, 'text failed'

    # else as text input
    param.value = np.inf
    assert infer_widget_metadata_for(param).get(Metadata.WIDGET_TYPE) == \
        WidgetType.TEXT_INPUT, 'else failed'
