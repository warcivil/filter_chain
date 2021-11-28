import sys
from jobs.default_job import FilterJob, AddJob

from pathlib import PurePath

INPUT_PATH = PurePath('/Users', 'sif', 'desktop', 'filter_chain', 'data_center_directory', 'input')
OUTPUT_PATH = PurePath('/Users', 'sif', 'desktop', 'filter_chain', 'data_center_directory', 'output')



# формат: name:job
JOB_SET = {
    'FIlterJob': FilterJob,
    #'AddJob':AddJob
}
if INPUT_PATH == OUTPUT_PATH:
    print(
        '[WARNING] пути для входных и выходных данных одинаковы, это приведет к дублированию проверок по уже проверенному файлу')
    choice = input('продолжить работу? (Y или N): ')
    if choice == 'N':
        sys.exit(0)
