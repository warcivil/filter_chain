from abc import ABC, abstractmethod


class AbstractJob(ABC):
    @abstractmethod
    def run_filters(self):
        pass

    @abstractmethod
    def job_description(self):
        pass
