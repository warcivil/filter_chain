from abc import ABC, abstractmethod


class AbstractJob(ABC):
    @abstractmethod
    def filter(self):
        pass

    @abstractmethod
    def job_description(self):
        pass
