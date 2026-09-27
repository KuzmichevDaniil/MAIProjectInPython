import argparse
from toolkit.calculator import calculation
from toolkit.errors import CalculatorErrors, ConverterErrors
from toolkit.converter import convertation
from toolkit.helper import table_help
import sys

def main(argv = None):
    parser = argparse.ArgumentParser(prog = "toolkit", add_help=False) #Создаем parser
    subparsers = parser.add_subparsers(dest = "command", required = True) #Создаем возмоность делать подкоманды и делаем их обязательными
    
    sub_calculator = subparsers.add_parser("calc", prefix_chars=" ", add_help=False) #Первая подкоманда calc
    sub_calculator.add_argument("expression")
    
    sub_convert = subparsers.add_parser("convert", add_help=False) #Вторая подкоманда convert
    sub_convert.add_argument("value")
    sub_convert.add_argument("--from", dest = "from_unit", required = True)
    sub_convert.add_argument("--to", dest = "to_unit", required = True)
    
    #Создаем кастомный --help
    if "--help" in sys.argv[1] or "--h" in sys.argv[1]:
            table_help()
            sys.exit(0)
    
    args = parser.parse_args() #Считывает аргументы и преобразует в объект Namespace 
    
    if args.command == "calc":
        try:
            print(calculation(args.expression)) #Вывести значение с аргумента expression(забираем выражение, которое ввели)
        except CalculatorErrors as err:
            print(str(err), file=sys.stderr)
            sys.exit(2)
    elif args.command == "convert":
        try:
            print(convertation(args.value, args.from_unit, args.to_unit))
        except ConverterErrors as err:
            print(str(err), file=sys.stderr)
            sys.exit(2)
    
            
if __name__ == "__main__":
    main()