import pytest


@pytest.mark.parametrize("hdl_input, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (25, "Low")])
def test_hdl_analysis(hdl_input, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(hdl_input)
    assert answer == expected


@pytest.mark.parametrize("ldl_input, expected", [
    (120, "Normal"),
    (133, "Borderline High"),
    (161, "High"),
    (190, "Very High")])
def test_ldl_analysis(ldl_input, expected):
    from blood_calculator import ldl_analysis
    answer = ldl_analysis(ldl_input)
    assert answer == expected
