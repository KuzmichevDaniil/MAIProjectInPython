from toolkit.errors import *
from re import *

def validation_calculator(tokens):
    check_empty(tokens)
    check_invalid_num_value(tokens)
    check_two_binary_operators(tokens)
    check_missing_operand(tokens)
    check_zero_operator(tokens)
    check_last_operator(tokens)
    
    
def validation_convert(value, from_unit, to_unit):
    check_incompatible_units(from_unit, to_unit)
    check_unknown_unit(from_unit, to_unit)
    check_invalid_num_value_for_convert(value)
    check_absolutely_zero(value, from_unit, to_unit)
    
    

def check_empty(tokens):
    '''Проверяю длину выполненной токенизации (если длина 0 - ошибка)'''
    if len(tokens) == 0:
        raise EmptyExpression

    
def check_invalid_character(expression):
    '''Проверяю, является ли текущий символ оператором, если нет - ошибка'''
    for token in expression:
        if not(token.isdigit()):
            if token not in ['+', '-', '*', '/', '(', ')', '.', ' ']:
                raise InvalidCharacter(token)
      

def check_invalid_num_value(tokens):
    '''Проверяю, если вещественное число записано неправильно, то ошибка'''
    for token in tokens:
        if match(r'^(\d+\.+)$', token) or match(r'^(\.+\d*)$', token) or match(r'^(\d+\.{2,}\d+)$', token): #проверка текущего токена по регулярному выражению, который выявляет неправильную запись вещественного числа
            raise InvalidNumericValue(token)


def check_two_binary_operators(tokens):
    '''Прохожусь по токенам: если следом за каким-либо опрератором следует другой оператор, то ошибка'''
    for token in range(len(tokens)-1):
        if (tokens[token] == '/' and tokens[token+1] == '/') or (tokens[token] == '+' and tokens[token+1] == '+')\
            or (tokens[token] == '-' and tokens[token+1] == '-') or (tokens[token] == '*' and tokens[token+1] == '*'):
                raise TwoBinaryOperators(tokens[token])

            
def check_missing_operand(tokens):
    '''
    Прохожусь по токенам: если после оператора, скобок идет другой оператор, скобка, 
    не схожий с первым оператором, скобкой (иначе была бы другая ошибка), то ошибка
    '''
    for token in range(len(tokens)-1):
        if ((tokens[token] in ['+', '-', '*', '/']) and (tokens[token+1] in ['+', '-', '*', '/']) and (tokens[token] != tokens[token+1]))\
            or (tokens[token] == '(' and tokens[token+1] == ')'):
            raise MissingOperand


def check_zero_operator(tokens):
    '''Проверяю, если выражение начинается с оператора, то ошибка'''
    if tokens[0] in ['+', '-', '*', '/']:
        raise ZeroOperator(tokens[0])


def check_last_operator(tokens):
    '''Проверяю, заканчивается ли выражение оператором, если да, то ошибка'''
    if tokens[-1] in ['+', '-', '*', '/']:
        raise LastOperator(tokens[-1])

        
def check_incompatible_units(fr_unit, to_unit):
    if (fr_unit in ['g', 'kg'] and to_unit not in ['g', 'kg'] and to_unit in ['mm', 'cm', 'm', 'km', 'c', 'k', 'f']) or\
        (fr_unit in ['mm', 'cm', 'm', 'km'] and to_unit not in ['mm', 'cm', 'm', 'km'] and to_unit in ['g', 'kg', 'c', 'k', 'f']) or\
            (fr_unit in ['c', 'k', 'f'] and to_unit not in ['c', 'k', 'f'] and to_unit in ['g', 'kg', 'mm', 'cm', 'm', 'km']):
                raise IncompatibleUnits(fr_unit, to_unit)


def check_unknown_unit(fr_unit, to_unit):
    if fr_unit in ['g', 'kg', 'mm', 'cm', 'm', 'km', 'c', 'k', 'f']:
        if to_unit not in ['g', 'kg', 'mm', 'cm', 'm', 'km', 'c', 'k', 'f']:
            raise UnknownUnit(to_unit)
    else:
        raise UnknownUnit(fr_unit)
        

def check_invalid_num_value_for_convert(value):
    if match(r'^(\d+\.+)$', value):
        raise InvalidNumericValueForConverter(value)
    elif  match(r'^(\.+\d*)$', value):
        raise InvalidNumericValueForConverter(value)
    elif match(r'^(\d+\.{2,}\d+)$', value):
        raise InvalidNumericValueForConverter (value)
    
def check_absolutely_zero(value, from_unit, to_unit):
    if from_unit in ['c', 'k', 'f'] and to_unit in ['c', 'k', 'f']:
        if float(value) < 0 and from_unit == 'k' and to_unit in ['f', 'c']:
            raise AbsolutelyZero(value)
        elif float(value) < -273.15 and from_unit == 'c' and to_unit in ['f', 'k']:
            raise AbsolutelyZero(value)
        elif float(value) < -459.67 and from_unit == 'f' and to_unit in ['c', 'k']:
            raise AbsolutelyZero(value)
        
