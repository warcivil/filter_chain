import sys

from functools import lru_cache
from jobs.abstract_job import AbstractJob
from jobs.base_job import RootJob
from managers.mixins.decorators import job_exception_output


class NumberFilterJob(RootJob, AbstractJob):
    @job_exception_output
    def handle(self):
        self.run_filters()
        super().handle()

    def run_filters(self):
        self.dataset_object.dataset = dict(filter(self.even_filter, self.dataset_object.dataset.items()))

    def even_filter(self, item):
        return type(item[1]) in (int,) and item[1] % 2 == 1

    def job_description(self):
        return f'данная JOB производит фильтрацию по числам'


class NoneFilterJob(RootJob, AbstractJob):
    @job_exception_output
    def handle(self):
        self.run_filters()
        super().handle()

    def run_filters(self):
        self.dataset_object.dataset = dict(filter(self.get_not_none_item, self.dataset_object.dataset.items()))

    def get_not_none_item(self, item):
        return item[1] is not None

    def job_description(self):
        return f'данная JOB работает с None значениями'


class KeyFilterJob(RootJob, AbstractJob):
    @job_exception_output
    def handle(self):
        self.run_filters()
        super().handle()

    def run_filters(self):
        self.dataset_object.dataset = dict(
            filter(self.get_item_consisting_of_string, self.dataset_object.dataset.items()))
        self.get_lower_key()

    def get_item_consisting_of_string(self, item):
        return isinstance(item[0], str) and item[0].isalpha()

    def get_lower_key(self):
        additional_dict = dict()
        for key, value in self.dataset_object.dataset.items():
            additional_dict[str.lower(key)] = value
        self.dataset_object.dataset = additional_dict

    def job_description(self):
        return f'данная JOB работает с ключами датасета'
