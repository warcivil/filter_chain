import sys
from filters.filters import get_even_dict, get_not_none_value_dict, get_dict_consisting_of_string
from pathlib import Path

INPUT_PATH = Path('C:/', 'Users', 'pixte', 'Desktop', 'filter_chain', 'input')
OUTPUT_PATH = Path('C:/', 'Users', 'pixte', 'Desktop', 'filter_chain', 'output')

FILTER_SET = [
    get_not_none_value_dict,
    get_even_dict,
    get_dict_consisting_of_string,
]

if INPUT_PATH == OUTPUT_PATH:
    print(
        'пути для входных и выходных данных одинаковы, это приведет к дублированию проверок по уже проверенному файлу')
    choice = input('продолжить работу? (Y или N): ')
    if choice == 'N':
        sys.exit(0)