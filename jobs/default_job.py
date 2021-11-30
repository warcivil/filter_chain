import sys

from functools import lru_cache
from jobs.base_job import RootJob
from managers.mixins.decorators import job_exception_output


class NumberFilterJob(RootJob):
    @job_exception_output
    def handle(self):
        for key in self.dataset_object.dataset.copy():
            if self.even_filter(self.dataset_object.dataset[key]):
                self.dataset_object.dataset.pop(key)
        super().handle()

    def even_filter(self, item):
        return type(item) in (int,) and item % 2 == 0  #

    def mod4_filter(self, item):
        return item % 4 == 0

    def job_description(self):
        return f'данная JOB работает с ключами датасета'


class NoneFilterJob(RootJob):
    @job_exception_output
    def handle(self):
        for key in self.dataset_object.dataset.copy():
            if self.get_not_none_item(self.dataset_object.dataset[key]):
                self.dataset_object.dataset.pop(key)
        super().handle()

    def get_not_none_item(self, item):
        return item is None

    def job_description(self):
        return f'данная JOB работает с None значениями'


class KeyFilterJob(RootJob):
    @job_exception_output
    def handle(self):
        for key in self.dataset_object.dataset.copy():
            if self.get_item_consisting_of_string(key):
                self.dataset_object.dataset.pop(key)
        self.get_lower_key()
        super().handle()

    def get_item_consisting_of_string(self, item):
        return not (isinstance(item, str) and item.isalpha())

    def get_lower_key(self):
        additional_dict = dict()
        for key, value in self.dataset_object.dataset.items():
            additional_dict[str.lower(key)] = value
        self.dataset_object.dataset = additional_dict

    def job_description(self):
        return f'данная JOB работает с ключами датасета'
