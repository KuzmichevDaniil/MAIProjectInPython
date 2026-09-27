from toolkit.validation import *
from cmd_history import save_to_json_file

def convert_to_lowercase(fr_ut, to_ut):
    '''Перевод единиц измерений к нижнему регистру с помощью .lower().
    Возвращаем две полученные единицы в нижнем регистре.'''
    fr_ut = fr_ut.lower()
    to_ut = to_ut.lower()
    return fr_ut, to_ut


def convertation(value, from_unit, to_unit):
    '''Переводим две единицы измерения в нижний регистр. Убираем пробелы в единицах измерения.
    Проверяем пример, единицы измерения на правильность(проводим валидацию).
    Создаем словарь, где ключ это соединение единиц измерения str(from_unit) + str(to_unit), а
    значение уже конвертация с помощью lambda функции.
    Но из метры m в mm и наоборот получаем "mmm", следовательно проверяем и добавляем
    знак "_", чтобы получить два ключа. После конвертации(переменная result) возвращаем полученный результат(result).'''
    from_unit, to_unit = convert_to_lowercase(from_unit, to_unit)
    
    from_unit = from_unit.replace(" ", "")
    to_unit = to_unit.replace(" ", "")
    
    validation_convert(value, from_unit, to_unit)
    
    if from_unit == 'm' and to_unit == 'mm':
        from_unit = 'm_'
    elif from_unit == 'mm' and to_unit == 'm':
        from_unit = 'mm_'
        
    units = {
        'gg': lambda x: x,
        'gkg': lambda x: x*0.001,
        'kgg': lambda x: x*1000,
        'kgkg': lambda x: x,
        'mmmm': lambda x: x,
        'mmcm': lambda x: x*0.1,
        'mm_m': lambda x: x*0.001,
        'mmkm': lambda x: x*0.000001,
        'cmmm': lambda x: x*10,
        'cmcm': lambda x: x,
        'cmm': lambda x: x*0.01,
        'cmkm': lambda x: x*0.00001,
        'm_mm': lambda x: x*1000,
        'mcm': lambda x: x*100,
        'mm': lambda x: x,
        'mkm': lambda x: x*0.001,
        'kmmm': lambda x: x*1000000,
        'kmcm': lambda x: x*100000,
        'kmm': lambda x: x*1000,
        'kmkm': lambda x: x,
        'cc': lambda x: x,
        'ck': lambda x: x+273.15,
        'cf': lambda x: (x*1.8) + 32,
        'kc': lambda x: x-273.15,
        'kk': lambda x: x,
        'kf': lambda x: ((x-273.15)*1.8) + 32,
        'fc': lambda x: ((x-32)*5)/9,
        'fk': lambda x: (((x-32)*5)/9) + 273.15,
        'ff': lambda x: x,
    }
    
    result = units[from_unit+to_unit](float(value))
    
    save_to_json_file(value, result, 'convert', from_unit, to_unit)
    
    return result