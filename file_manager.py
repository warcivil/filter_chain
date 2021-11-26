import json
import os
import sys
from functools import wraps

from config import INPUT_PATH, OUTPUT_PATH


def exception_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f'Произошла ошибка в методе {func.__name__}. Код ошибки:')
            print(str(exc))
            sys.exit(0)
        return result
    return wrapper


class FileManager:
    def __init__(self):
        print(f'Проверка существования путей:\n{INPUT_PATH}\n{OUTPUT_PATH}')
        if not os.path.exists(INPUT_PATH):
            print(f'директории по пути {INPUT_PATH} не существует')
            sys.exit(0)
        if not os.path.exists(OUTPUT_PATH):
            print(f'директории по пути {OUTPUT_PATH} не существует')
            sys.exit(0)
        print(f'Директории существуют. Продолжение работы')

    def _get_file(self):
        for file in os.listdir(INPUT_PATH):
            if file.endswith('.json'):
                yield file
        print('в папке больше не найдено json файлов. завершение работы')
        print(f'отформатированный файл сохранен в {OUTPUT_PATH}')
        sys.exit(0)

    def get_data_and_filename(self):
        json_files = self._get_file()
        for json_file in json_files:
            @exception_output
            def get_dict_data():
                with open(str(INPUT_PATH) + '\\' + json_file, mode='r') as handle:
                    return json.loads(handle.read())

            yield get_dict_data(), json_file

    @exception_output
    def save_data(self, filename, data):
        with open(str(OUTPUT_PATH) + '\\' + 'output_' + filename, mode='w') as handle:
            data = json.dumps(data)
            handle.write(data)


file_manager = FileManager()
