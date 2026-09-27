from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.padding import Padding

#Создаем главный объект управления терминалом
console = Console()

#Создаем словарь, где храним всю информацию про наши команды.
commands = {
    'calc "EXPRESSION"': {
        'desc': "Вычисление математических выражений",
        'flags': {
                "-":"-"
            },
    },
    
    'convert VALUE': {
        'desc': "Конвертация единиц измерения",
        'flags':{
            '--from UNIT': "Указать из какой единицы конвертировать",
            '--to UNIT': "Указать в какую единицу конвертировать",
        }
    },
    
    '-':{
        'desc': "-",
        'flags':{
            '--help': "Выводит информацию про доступные команды."
        }
    }
} 

def padding_add(text):
    '''Добавляем тексту в таблице отступ снизу.'''
    return Padding(text, (0,0,1,0))

def table_help():
    '''Создаем help-таблицу: в переменной table хранится сама таблица, где мы создаем заголовок,
    стиль для заголовка, убираем границы между столбцами. Добавляем столбцы
    с помощью add_column, где задаем заголовок столбца, стиль текста и ширину столбца.
    Проходимся по словарю и вытаскиваем из него всю информацию сначала про calc, потом про convert:
    с помощью enumerate() узнаем index и, если он первый, то добавляем в столбцы сначала общую информацию про калькулятор и конвертер:
    как вызываются команды и их описания. Потом уже внутри самих команд, если index больше 0, ищем информацию про 
    флаги и добавляем их столбцы с флагами и описанием этих флагов(добавление в столбец .add_row()).
    После выводим help-таблицу, указывая цвет рамки и растягиваемость таблицы(False - сжать под контент, True - растянуть таблицу на всю ширину).'''
    table = Table(
        title=padding_add("[bold green]СПИСОК ДОСТУПНЫХ КОМАНД[/bold green]"),
        title_style="bold",
        show_lines=True,
        box = None
    )
    
    table.add_column(padding_add("Команда"), style = 'green bold', width=30)
    table.add_column(padding_add("Описание"), style = 'white bold', width=30)
    table.add_column(padding_add("Флаг"), style = 'green bold', width=30)
    table.add_column(padding_add("Описание"), style = 'white bold', width=30)
    
    for cmd, inf in commands.items():
        for index, (flags_cmd, flags_desc) in enumerate(inf['flags'].items()):
            if index == 0:
                table.add_row(cmd, padding_add(inf['desc']), flags_cmd, padding_add(flags_desc))
            else:
                table.add_row("", "", flags_cmd, padding_add(flags_desc))
                
    console.print(Panel(table, border_style="white", expand=False))
    
