import pytest

@pytest.mark.parametrize("hdl_input, expected",
    [(65, "Normal"),
     (45, "Borderline Low"),
     (25, "Low")])
def test_hdl_analysis(hdl_input, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(hdl_input)
    assert answer == expected
    
    
