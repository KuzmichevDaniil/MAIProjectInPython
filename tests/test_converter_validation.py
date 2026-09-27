import pytest
from toolkit.converter import convertation

from toolkit.errors import (
    IncompatibleUnits,
    UnknownUnit,
    InvalidNumericValueForConverter,
    AbsolutelyZero
)


@pytest.mark.parametrize("examp, fr, to", [
    ("1213", "kg", "m"),
    ("323", "m", "c"),
    ("4566", "f", "m"),
    ("87978", "g", "k")
    ])
def test_incompatible_units(examp, fr, to):
    with pytest.raises(IncompatibleUnits):
        convertation(examp, fr, to)

        
@pytest.mark.parametrize("examp, fr, to", [
    ("675", "H", "kH"),
    ("6546", "L", "mmL"),
    ("33", "dj", "kdj"),
    ("767", "dptr", "dptr")
    ])
def test_unknow_unit(examp, fr, to):
    with pytest.raises(UnknownUnit):
        convertation(examp, fr, to)


@pytest.mark.parametrize("examp, fr, to", [
    ("342..", "mm", "m"),
    ("324...32442", "m", "cm"),
    ("...4566", "kg", "g"),
    ("87....978", "c", "f")
    ])
def test_uinvalid_numeric_for_converter(examp, fr, to):
    with pytest.raises(InvalidNumericValueForConverter):
        convertation(examp, fr, to)


@pytest.mark.parametrize("examp, fr, to", [
    ("-273.897", "c", "k"),
    ("-500", "f", "c"),
    ("-2", "k", "f")
    ])
def test_absolutely_zero(examp, fr, to):
    with pytest.raises(AbsolutelyZero):
        convertation(examp, fr, to)