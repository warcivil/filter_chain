import json
import os
import sys

from configs.config import INPUT_PATH, OUTPUT_PATH

from .mixins.exception_output_decorator import exception_output
from .mixins.os_platform_mixin import OsPlatformMixin


class FileManager(OsPlatformMixin):
    def __new__(cls, *args, **kwargs):
        print(f'Проверка существования путей:\n{INPUT_PATH}\n{OUTPUT_PATH}')
        if not os.path.exists(INPUT_PATH):
            print(f'[ERROR] директории по пути {INPUT_PATH} не существует')
            print('Поменять путь до директории можно в configs/config.py')
            sys.exit(0)
        if not os.path.exists(OUTPUT_PATH):
            print(f'[ERROR] директории по пути {OUTPUT_PATH} не существует')
            print('Поменять путь до директории можно в configs/config.py')
            sys.exit(0)
        print(f'Директории существуют. Продолжение работы')
        instance = super(FileManager, cls).__new__(cls, *args, **kwargs)
        return instance
    def __init__(self):
        self.slash = super().get_correct_slash()

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
                with open(str(INPUT_PATH) + self.slash + json_file, mode='r') as handle:
                    return json.loads(handle.read())

            yield get_dict_data(), json_file

    @exception_output
    def save_data(self, filename, data):
        with open(str(OUTPUT_PATH) + self.slash + 'output_' + filename, mode='w') as handle:
            data = json.dumps(data)
            handle.write(data)


file_manager = FileManager()
