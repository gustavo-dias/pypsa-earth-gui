"""Tests for module datetime.py"""

from pytest import raises

from app.helpers.datetime import get_date_in_isoformat


def test_get_date_in_isoformat() -> None:
    """"""
    assert get_date_in_isoformat("2026-07-02") == "2026-07-02T00:00:00"

    with raises(ValueError):
        get_date_in_isoformat("2026/07/02")

    with raises(ValueError):
        get_date_in_isoformat("02-07-2026")

    with raises(AttributeError):
        get_date_in_isoformat(2026) # type: ignore
