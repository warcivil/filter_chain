import sys

from configs.config import FILTER_SET, JOB_SET, OUTPUT_PATH
from jobs.base_job import RootJob
from managers.file_manager import file_manager


class FilterService:
    def __init__(self):
        self.filter_set = FILTER_SET
        self.datasets = file_manager.get_data_and_filename()

    def job_setup(self):
        print('выполнение задач\n')
        dataset, filename = next(self.datasets)
        dataset_object = DatasetObject(dataset=dataset, filename=filename)
        root = RootJob(dataset_object)
        print('выполняется предварительная настройка цепочки JOB и попытка прохода по 1 датасету')
        for job_name_key in JOB_SET.keys():
            new_job = JOB_SET[job_name_key](dataset_object)
            root.add_modifier(new_job)
            print(f'добавлена новая JOB, {job_name_key}')
            print(f'описание JOB: {new_job.job_description()}\n')
        print(dataset_object)
        root.handle()
        file_manager.save_data(filename, dataset_object.get_dataset())
        print(f'JOBS {FilterService.get_jobs_name_list()} выставлены в цепочку, выполняется их запуск')
        print(f'{filename} успешно проведен через все JOB и записан в {OUTPUT_PATH}\n')
        return root

    def filter_chain(self):
        root = self.job_setup()
        for dataset, filename in self.datasets:
            dataset_object = DatasetObject(dataset=dataset, filename=filename)
            root.set_dataset_object(dataset_object=dataset_object)
            print(dataset_object)
            root.handle()
            file_manager.save_data(filename, dataset_object.get_dataset())
            print(f'{filename} успешно проведен через все JOB и записан в {OUTPUT_PATH}\n')

    @staticmethod
    def get_jobs_name_list() -> list:
        return [job_name_key for job_name_key in JOB_SET]


class DatasetObject:
    def __init__(self, dataset, filename):
        self.dataset = dataset
        self.filename = filename
        self.filters = FILTER_SET

    def __str__(self) -> str:
        return f'имя датасета {self.filename}'

    def get_dataset(self):
        return self.dataset


if __name__ == '__main__':
    filter_service = FilterService()
    filter_service.filter_chain()
