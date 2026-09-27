from toolkit.tokenizator import expression_to_tokens
from decimal import Decimal, ROUND_HALF_UP
from toolkit.validation import *
from cmd_history import save_to_json_file
from toolkit.errors import DivisionByZero


def expression_to_rpn(tk):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    
    for token in tk:
        if token == '(':
            stack.append(token)
            
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()
                
        elif token in operators:
            while stack and stack[-1] in operators and operators[stack[-1]] >= operators[token]:
                output.append(stack.pop())
            stack.append(token)
            
        else: 
            output.append(token)
    
    while stack:
        output.append(stack.pop())
            
    return output


def calculation(expr):
    tokens = expression_to_tokens(expr)

    check_invalid_character(expr)
    validation_calculator(tokens)
    
    pre_tokens_rpn = expression_to_rpn(tokens)
    tokens_rpn = [tokens for tokens in pre_tokens_rpn if tokens != ""]

    operators = {'+': lambda a, b: Decimal(a) + Decimal(b), 
                 '-': lambda a, b: Decimal(a) - Decimal(b), 
                 '*': lambda a, b: Decimal(a) * Decimal(b), 
                 '/': lambda a, b: Decimal(a) / Decimal(b)}
    
    stack = []
    
    for token in tokens_rpn:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "/" and (b == 0 or b == '0' or b == '0.0'):
                raise DivisionByZero
            
            result = operators[token](a, b)
            stack.append(result)
        
        else: 
            stack.append(token)
    
    result_stack = stack[0]
    save_to_json_file(expr, stack[0], 'calc')

    result = result_stack.quantize(Decimal('0.00001'), rounding = ROUND_HALF_UP)
    
    reg_1 = r'(?!000[1-9]0)(?!00[1-9]00)(?!0[1-9]000)(?!0[1-9][1-9]00)(?!0[1-9][1-9][1-9]0)'
    reg_2 = r'(?![1-9][1-9][1-9][1-9]0)(?![1-9][1-9][1-9]00)(?![1-9][1-9]000)(?![1-9]0000)'
    reg_result_1 = r'\d+\.(?!00000)' + f'{reg_1}{reg_2}' + r'\d{5}'
    
    reg_4 = r'[1-9][1-9][1-9][1-9]0|[1-9][1-9][1-9]00|[1-9][1-9]000|[1-9]0000'
    reg_5 = r'000[1-9]0|00[1-9]00|0[1-9]000|0[1-9][1-9]00|0[1-9][1-9][1-9]0'
    reg_result_2 = r'\d+\.' + f'(?:{reg_4}|{reg_5})'
    
    if match(reg_result_1, str(result)):
        return result
    elif match(reg_result_2, str(result)):
        return float(result)
    else:
        return int(result)
