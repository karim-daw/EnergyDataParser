from hello.myMethods import convert_kwh_to_gj

import pytest


def test_positive_conversion():
    result = convert_kwh_to_gj(100)
    assert result == 0.36


def test_zero_conversion():
    result = convert_kwh_to_gj(0)
    assert result == 0


def test_negative_conversion():
    with pytest.raises(ValueError):
        convert_kwh_to_gj(-100)
