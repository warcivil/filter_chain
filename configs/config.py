import pathlib
import sys
from filters.default_filters import get_even_dict, get_not_none_value_dict, get_dict_consisting_of_string
from jobs.default_job import FilterJob

from pathlib import PurePath

INPUT_PATH = PurePath('/Users', 'sif', 'desktop', 'filter_chain', 'data_center_directory', 'input')
OUTPUT_PATH = PurePath('/Users', 'sif', 'desktop', 'filter_chain', 'data_center_directory', 'output')

FILTER_SET = [
    get_not_none_value_dict,
    get_even_dict,
    get_dict_consisting_of_string,
]


# формат: name:job
JOB_SET = {
    'FIlterJob': FilterJob,
}
if INPUT_PATH == OUTPUT_PATH:
    print(
        '[WARNING] пути для входных и выходных данных одинаковы, это приведет к дублированию проверок по уже проверенному файлу')
    choice = input('продолжить работу? (Y или N): ')
    if choice == 'N':
        sys.exit(0)
