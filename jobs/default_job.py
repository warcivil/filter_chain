import sys

from jobs.abstract_job import AbstractJob
from jobs.base_job import RootJob
from managers.mixins.decorators import job_exception_output


class FilterJob(RootJob, AbstractJob):
    @job_exception_output
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

    def job_description(self):
        return f'эта JOB предназначена для прохода json файла по фильтрам.\nПоставлены фильтры: {self.get_filters_name()}'

    def get_filters_name(self):
        return [filter.__name__ for filter in self.dataset_object.filters]


class AddJob(RootJob, AbstractJob):
    @job_exception_output
    def handle(self):
        self.add_in_dataset()
        super().handle()

    def add_in_dataset(self):
        self.dataset_object.dataset['name'] = 100

    def job_description(self):
        return f'эта JOB которая создает поле name и ложит туда 100'
