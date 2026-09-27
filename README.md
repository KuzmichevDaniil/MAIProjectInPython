# Лабораторная работа №1. Программироание на Python

>Калькулятор и конвертер величин

---

## Что умеет программа

### Калькулятор
- Поддерживаемые операторы: `+`, `-`, `/`, `*` .
- Поддерживает унарный `+` и `-` перед числом.
- Возможность писать выражения в скобках.
- Соблюдается приоритет `*` и `/` над `+` и `-`.
- Поддерживает целые и вещественные числа.

### Конвертер 
- Поддерживает группы единиц: 
    - `g`, `kg` - масса
    - `mm`, `cm`, `m`, `km` - длина
    - `c`, `f`, `k` - температура (Градусы, Фаренгейт, Кельвины)

- Не допускается температура ниже абсолютного нуля!
    - < -273.15 при переводе с градусов (с)
    - < -459.67 при переводе с фаренгейтов (f)
    - < 0 пр переводе с кельвинов (k)

### История вычислений

- История успешных операций сохраняется в файле ***calc_and_convert_history.json***:
    `lab_01\calc_and_convert_history.json`

---

## Структура проекта

```text
lab_01/
  pyproject.toml
  README.md
  cmd_history.py
  calc_and_convert_history.json
  src/toolkit/
    __init__.py
    __main__.py
    calculator.py
    converter.py
    errors.py
    helper.py
    tokenizator.py
    validation.py
  tests/
    test_calculator_validation.py
    test_calculator.py
    test_converter_validation.py
    test_converter.py
```

---

## Команды для запуска программы

```bash
python -m toolkit calc "EXPRESSION"
python -m toolkit convert VALUE --from UNIT --to UNIT
python -m toolkit --help
```

---

## Возможные ошибки

### Калькулятор
| Ошибка | Описание |
|---|---|
| `EmptyExpression` | Передано пустое выражение |
| `InvalidCharacter` | Недопустимое значение |
| `MissingOperand` | Пропущен какой-либо операнд |
| `TwoBinaryOperators` | Два бинарных оператора подряд |
| `DivisionByZero` | Деление на ноль |
| `InvalidNumericValue` | Неверное числовое значение |
| `ZeroOperator` | Выражение не должно начинаться с оператора |
| `LastOperator` | Выражение не должно заканчиваться оператором |

### Конвертер
| Ошибка | Описание |
|---|---|
| `IncompatibleUnits` | Несовместимые единицы |
| `UnknownUnit` | Неизвестная единица |
| `InvalidNumericValueForConverter` | Неверное числовое значение |
| `AbsolutelyZero` | Температура ниже абсолютного нуля |

---

## Клонирование 

### Установка 

```bash
git clone https://github.com/KuzmichevDaniil/MAIProjectInPython.git
```
