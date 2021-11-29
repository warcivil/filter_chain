import sys
from jobs.default_job import NumberFilterJob, NoneFilterJob, KeyFilterJob

from pathlib import PurePath
import logging

logging.basicConfig(level=logging.DEBUG)


INPUT_PATH = PurePath('/Users', 'sif', 'desktop', 'filter_chain', 'data_center_directory', 'input')
OUTPUT_PATH = PurePath('/Users', 'sif', 'desktop', 'filter_chain', 'data_center_directory', 'output')

# формат: name:job
JOB_SET = {
    'NoneFilterJob': NoneFilterJob,
    'NumberFilterJob': NumberFilterJob,
    'KeyFilterJob': KeyFilterJob
}
if INPUT_PATH == OUTPUT_PATH:
    logging.warning(
        ' пути для входных и выходных данных одинаковы, это приведет к дублированию проверок по уже проверенному файлу')
    choice = input('продолжить работу? (Y или N): ')
    if choice == 'N':
        sys.exit(0)
