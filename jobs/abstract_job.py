from abc import ABC, abstractmethod


class AbstractJob(ABC):
    @abstractmethod
    def job_description(self):
        pass
