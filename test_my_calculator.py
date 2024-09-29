import pytest


def test_sqrt_raise_ValueError():
    from my_calculator import sqrt
    input_value = 4
    with pytest.raises(ValueError):
        answer = sqrt(input_value)
        
        
def test_sqrt():

