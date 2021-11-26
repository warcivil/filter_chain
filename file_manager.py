import json
import os
import sys

from config import INPUT_PATH, OUTPUT_PATH


class FileManager:
    def __init__(self):
        print(f'Проверка существования путей')
        if not os.path.exists(INPUT_PATH):
            print(f'директории по пути {INPUT_PATH} не существует')
            sys.exit(0)
        if not os.path.exists(OUTPUT_PATH):
            print(f'директории по пути {OUTPUT_PATH} не существует')
            sys.exit(0)

    def _get_file(self):
        self.check_folder_exists(INPUT_PATH)
        for file in os.listdir(INPUT_PATH):
            if file.endswith('.json'):
                yield file

    def get_data_and_filename(self):
        json_files = self._get_file()
        for json_file in json_files:
            self.check_folder_exists(INPUT_PATH)
            with open(str(INPUT_PATH) + '\\' + json_file, mode='r') as handle:
                try:
                    data = json.loads(handle.read())
                    yield data, json_file
                except Exception as exp:
                    print('Произошла ошибка в методе get_data. Код ошибки:')
                    print(str(exp))
                    sys.exit(0)

    def save_data(self, filename, data):
        self.check_folder_exists(OUTPUT_PATH)
        with open(str(OUTPUT_PATH) + '\\' + 'output_' + filename, mode='w') as handle:
            try:
                data = json.dumps(data)
                handle.write(data)
            except Exception as exp:
                print('Произошла ошибка в методе save_data. Код ошибки:')
                print(str(exp))
                sys.exit(0)

file_manager = FileManager()
