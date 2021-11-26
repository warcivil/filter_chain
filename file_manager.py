import json
import os
import sys

from config import INPUT_PATH, _get_file, OUTPUT_PATH


class FileManager:
    def _get_file(self):
        for file in os.listdir(INPUT_PATH):
            if file.endswith('.json'):
                yield file

    def get_data_and_filename(self):
        json_files = self._get_file()
        for json_file in json_files:
            with open(str(INPUT_PATH) + '\\' + json_file, mode='r') as handle:
                try:
                    data = json.loads(handle.read())
                    yield data, json_file
                except Exception as exp:
                    print('get_data')
                    print(str(exp))
                    sys.exit(0)

    def save_data(self, filename, data):
        with open(str(OUTPUT_PATH) + '\\' + 'output_' + filename, mode='w') as handle:
            try:
                data = json.dumps(data)
                handle.write(data)
            except Exception as exp:
                print('save_data')
                print(str(exp))
                sys.exit(0)


file_manager = FileManager()
