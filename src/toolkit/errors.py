class CalculatorErrors(Exception):
    pass

class ConverterErrors(Exception):
    pass

class EmptyExpression(CalculatorErrors):
    def __init__(self):
        super().__init__("Пустое выражение.")
        
class InvalidCharacter(CalculatorErrors):
    def __init__(self, character):
        super().__init__(f"Недопустимое значение {character} .")
        
class MissingOperand(CalculatorErrors):
    def __init__(self):
        super().__init__(f"Пропущен операнд.")

class TwoBinaryOperators(CalculatorErrors):
    def __init__(self, operators ):
        super().__init__(f"Два бинарных оператора {operators} подряд.")
        
class DivisionByZero(CalculatorErrors):
    def __init__(self):
        super().__init__("Деление на ноль.")

class InvalidNumericValue(CalculatorErrors):
    def __init__(self, value):
        super().__init__(f"Неверное числовое значение {value}")
        
class ZeroOperator(CalculatorErrors):
    def __init__(self, operator):
        super().__init__(f"Выражение не должно начинаться с {operator}, пропущен операнд!")
        
class LastOperator(CalculatorErrors):
    def __init__(self, operator):
        super().__init__(f"Выражение не должно заканчиваться оператором {operator}, пропущен операнд!")
        
class IncompatibleUnits(ConverterErrors):
    def __init__(self, unit_from, unit_to):
        super().__init__(f"Несовместимые единицы {unit_from} и {unit_to}. Конвертация между разными группами единиц запрещена!")
        
class UnknownUnit(ConverterErrors):
    def __init__(self, unit):
        super().__init__(f"Неизвестная единица {unit} .")
        

class InvalidNumericValueForConverter(ConverterErrors):
    def __init__(self, value):
        super().__init__(f"Неверное числовое значение {value}")
        

class AbsolutelyZero(ConverterErrors):
    def __init__(self, value):
        super().__init__(f"Температура ниже абсолютного нуля: {value}!")
        