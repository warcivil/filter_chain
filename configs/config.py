from os import path
import sys
from jobs.default_job import FilterJob, AddJob

from pathlib import PurePath, Path

AUTO_PATH = True

if AUTO_PATH:
    INPUT_PATH = str(Path.cwd()) + '/data_center_directory/input/'
    OUTPUT_PATH = str(Path.cwd()) + '/data_center_directory/output/'
else:
    INPUT_PATH = Path('/home', 'achupakhin', 'desktop', 'filter_chain', 'input')
    OUTPUT_PATH = Path('/home', 'achupakhin', 'desktop', 'filter_chain', 'outpu/')

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
