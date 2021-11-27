import sys

from configs.config import FILTER_SET, OUTPUT_PATH
from managers.file_manager import file_manager


class FilterService:
    def __init__(self):
        self.filter_set = FILTER_SET

    def filter_chain(self):
        print('выполнение задач')
        datasets = file_manager.get_data_and_filename()
        for dataset, filename in datasets:
            dataset_object = DatasetObject(dataset=dataset, filename=filename)
            root = DatasetObjectModifier(dataset_object)
            print(dataset_object)
            root.add_modifier(FilterModifier(dataset_object))
            print('все модификаторы выставлены в цепочку, выполняется их запуск')
            root.handle()
            file_manager.save_data(filename, dataset_object.get_dataset())
            print(f'{filename} успешно проведен через все модификаторы и записан в {OUTPUT_PATH}')

class DatasetObject:
    def __init__(self, dataset, filename):
        self.dataset = dataset
        self.filename = filename
        self.filters = FILTER_SET

    def __str__(self) -> str:
        return f'имя датасета {self.filename}, поставлены фильтры: {self.get_filters_name()}'

    def get_dataset(self):
        return self.dataset

    def get_filters_name(self):
        return [filter.__name__ for filter in self.filters]


class DatasetObjectModifier:
    def __init__(self, dataset_object):
        self.dataset_object = dataset_object
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class FilterModifier(DatasetObjectModifier):
    def handle(self):
        self.change_filter_data()
        super().handle()

    def change_filter_data(self):
        for filter in self.dataset_object.filters:
            try:
                self.dataset_object.dataset = filter(self.dataset_object.dataset)
            except Exception as exc:
                print(f"произошла ошибка в фильтре {self.dataset_object.filter.__name__}")
                print(f"текст ошибки {str(exc)}")
                choice = input('продолжить работу (Y или N)?: ')
                if choice == 'N':
                    sys.exit(0)

if __name__ == '__main__':
    filter_service = FilterService()
    filter_service.filter_chain()
