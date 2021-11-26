import sys

from config import FILTER_SET, OUTPUT_PATH
from file_manager import file_manager


class CleanManager:
    def __init__(self):
        self.filter_set = FILTER_SET

    def filter_chain(self):
        print('выполнение задач')
        datasets = file_manager.get_data_and_filename()
        for dataset, filename in datasets:
            for filter in self.filter_set:
                dataset = self.get_filter_data(filter, dataset)
                file_manager.save_data(filename, dataset)

    def get_filter_data(self, filter, dataset):
        try:
            dataset = filter(dataset)
            return dataset
        except Exception as exc:
            print(f"произошла ошибка в фильтре {filter.__name__}")
            print(f"текст ошибки {str(exc)}")
            choice = input('продолжить работу (Y или N)?: ')
            if choice == 'Y':
                return dataset
            sys.exit(0)


clean_manager = CleanManager()
clean_manager.filter_chain()
