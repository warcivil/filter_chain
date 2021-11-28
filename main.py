from configs.config import JOB_SET, OUTPUT_PATH
from configs.job_config.filter_job_config import FILTER_SET
from jobs.base_job import RootJob
from managers.file_manager import file_manager
from managers.mixins.decorators import exception_output


class DatasetObject:
    def __init__(self, dataset, filename) -> None:
        self.dataset = dataset
        self.filename = filename

    def __str__(self) -> str:
        return f'{self.filename}'

    def get_dataset(self) -> dict:
        return self.dataset

    def set_new_dataset(self, dataset, filename) -> None:
        self.dataset = dataset
        self.filename = filename

    def save_dataset(self) -> None:
        file_manager.save_data(self.filename, self.dataset)


class FilterService:
    def __init__(self) -> None:
        self.datasets = file_manager.get_data_and_filename()

    @exception_output
    def job_setup(self) -> tuple[RootJob, DatasetObject]:
        print('выполнение задач\n')
        dataset, filename = next(self.datasets)
        print('создается корневая JOB, так же создается обьект для хранения датасетов')
        dataset_object = DatasetObject(dataset=dataset, filename=filename)
        root = RootJob(dataset_object)
        print('выполняется предварительная настройка цепочки JOB и попытка прохода по 1 датасету\n')

        for job_name_key in JOB_SET.keys():
            new_job = JOB_SET[job_name_key](dataset_object)
            root.add_modifier(new_job)
            print(f'добавлена новая JOB, {job_name_key}')
            print(f'описание JOB: {new_job.job_description()}\n')

        print(dataset_object)
        root.handle()
        dataset_object.save_dataset()
        print(f'JOBS {FilterService.get_jobs_name_list()} выставлены в цепочку, выполняется их запуск')
        print(f'{filename} успешно проведен через все JOB и записан в {OUTPUT_PATH}\n')
        return root, dataset_object

    @exception_output
    def filter_chain(self) -> None:

        root, dataset_object = self.job_setup()  # выполнение 1 задачи и создание цепочки всех job
        for dataset, filename in self.datasets:
            dataset_object.set_new_dataset(filename=filename, dataset=dataset)
            print(f'выполняется работа над датасетом: {dataset_object}')
            root.handle()
            dataset_object.save_dataset()
            print(f'{filename} успешно проведен через все JOB и записан в {OUTPUT_PATH}\n')

    @staticmethod
    def get_jobs_name_list() -> list:
        return [job_name_key for job_name_key in JOB_SET]


if __name__ == '__main__':
    filter_service = FilterService()
    filter_service.filter_chain()
