import pytest
from toolkit.calculator import calculation

from toolkit.errors import (
    EmptyExpression,
    InvalidCharacter,
    MissingOperand,
    TwoBinaryOperators,
    DivisionByZero,
    InvalidNumericValue,
    ZeroOperator,
    LastOperator
)


@pytest.mark.parametrize("expr", ["          ", " "])
def test_empty_expression(expr):
    with pytest.raises(EmptyExpression):
        calculation(expr)

        
@pytest.mark.parametrize("expr", ["13123$323", "7584@4595", "23342#354353, 2+a"])
def test_invalid_character(expr):
    with pytest.raises(InvalidCharacter):
        calculation(expr)

        
@pytest.mark.parametrize("expr", ["13123+*3242", "2*/3", "23342+-+32242542", "234423+()*252532"])
def test_missing_operand(expr):
    with pytest.raises(MissingOperand):
        calculation(expr)

        
@pytest.mark.parametrize("expr", ["1+++3", "1412**231", "13123---23"])
def test_two_binary_operators(expr):
    with pytest.raises(TwoBinaryOperators):
        calculation(expr)

        
@pytest.mark.parametrize("expr", ["1/((23+443)*0)", "1/0", "2323/(12*0)"])
def test_division_by_zero(expr):
    with pytest.raises(DivisionByZero):
        calculation(expr)
        
@pytest.mark.parametrize("expr", ["13+3244...34242*34", "15*...0+3", "55*0..+3"])
def test_invalid_numeric_value(expr):
    with pytest.raises(InvalidNumericValue):
        calculation(expr)
        

@pytest.mark.parametrize("expr", ["--231+343", "/2432+3", "*+34242/342", "++4234/243"])
def test_zero_operator(expr):
    with pytest.raises(ZeroOperator):
        calculation(expr)
        
@pytest.mark.parametrize("expr", ["233+(90+3)-", "234/442*343+", "34423-543*", "242*0.54/"])
def test_last_operator(expr):
    with pytest.raises(LastOperator):
        calculation(expr)