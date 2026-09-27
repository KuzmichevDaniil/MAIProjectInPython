import pytest
from toolkit.converter import convertation

@pytest.mark.parametrize('example, fr, to, result', [
    ("1000", "mm", "m", 1.0),
    ("123", "km", "m", 123000.0),
    ("4345", "cm", "m", 43.45),
    ("532", "cm", "mm", 5320.0),
    ("6767", "mm", "km", 0.006767),
    ("99", "m", "cm", 9900.0),
    ("123456", "m", "m", 123456.0)
    
])
def test_convertation_for_length(example, fr, to, result):
    assert convertation(example, fr, to) == pytest.approx(result)
    
    
@pytest.mark.parametrize('example, fr, to, result', [
    ("1.5", "kg", "g", 1500.0),
    ("0.3", "kg", "g", 300.0),
    ("15", "kg", "g", 15000.0),
    ("500", "g", "kg", 0.5),
    ("4500", "g", "kg", 4.5),
    ("75", "g", "kg", 0.075),
    ("5", "kg", "kg", 5.0),
    ("25", "g", "g", 25.0)
])
def test_convertation_for_weight(example, fr, to, result):
    assert convertation(example, fr, to) == pytest.approx(result)
    

@pytest.mark.parametrize('example, fr, to, result', [
    ("0", "c", "f", 32.0),
    ("-273.15", "c", "k", 0.0),
    ("20", "c", "f", 68.0),
    ("98.6", "f", "c", 37.0),
    ("2424", "f", "f", 2424.0),
    ("373.15", "k", "f", 212.0),
    ("1", "c", "c", 1.0)
])
def test_convertation_for_temperature(example, fr, to, result):
    assert convertation(example, fr, to) == pytest.approx(result)
    
