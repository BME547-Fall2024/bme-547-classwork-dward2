import pytest


def test_sqrt_raise_ValueError():
    from my_calculator import sqrt
    input_value = -4
    with pytest.raises(ValueError):
        answer = sqrt(input_value)


def test_sqrt_raise_TypeError():
    from my_calculator import sqrt
    input_value = "4"
    with pytest.raises(TypeError):
        answer = sqrt(input_value)


def test_sqrt():
    from my_calculator import sqrt
    answer = sqrt(4)
    assert answer == 2
