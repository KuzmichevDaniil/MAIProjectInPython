import json
import os
from datetime import datetime

#Прописываем путь к JSON файлу 
calc_and_convert_hist = "calc_and_convert_history.json"


def save_to_json_file(expression, result, cmd, from_unit = "", to_unit = ""):
    '''На вход функции подается обязательные аргументы примера, результата, типа команды нашего приложения.
    Если команда "calc", то мы заполняем историю без from_unit и to_unit. Если же команда "convert", то 
    история уже будет заполнятся с aргументами from_unit и to_unit. С помощью os.path.exists() проверяем, есть ли
    уже JSON файл "calc_and_convert_history.json": если да, то мы считываем JSON-текст из файла с помошью json.load() 
    и превращает его в обычный список Python (у нас это список history); если произойдет какая-либо ошибка, то мы просто 
    ничего в JSON файл записывать не будем. После преобразования и проверки на ошибки мы добавляем нашу историю в список 
    history, открываем файл и записываем историю в него.'''
    if cmd == 'calc':
        new_hist = {
            "command": cmd,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "expression": str(expression),
            "result": str(result)
        }
    
    elif cmd == 'convert':
        new_hist = {
            "command": cmd,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "value": str(expression),
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": str(result)
        }
    
    if os.path.exists(calc_and_convert_hist):
        with open(calc_and_convert_hist, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []
    else: 
        history = []
        
    history.append(new_hist)
    
    with open(calc_and_convert_hist, 'w', encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)