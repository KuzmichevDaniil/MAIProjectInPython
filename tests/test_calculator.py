import pytest
from toolkit.calculator import calculation

@pytest.mark.parametrize("expression, result", [
    ("2+3*4", 14),
    ("10 / 4", 2.5),
    ("-2 * -3", 6),
    ("1+-2", -1),
    ("2+5+3/24+52", 59.125),
    ("1+2", 3),
    ("-136 ++ 25266++24.3 -4 *+4-+5- -0.6", 25133.9),
    ("-0.1+45*34", 1529.9),
    ("3454+343-234.3453*657", -150167),
    ("200/40+5.67*9", 56.03)
    
    
])

def test_calculation(expression, result):
    assert calculation(expression) == pytest.approx(result)