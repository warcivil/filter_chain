[WINDOWS] python main.py

[OS X / LINUX] python3 main.py


Фильтры здесь представлены в виде Job(задач, работ) то есть каждая новая job - это новый пул фильтров, пример job:

```python
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
```
то есть очередная job это некий пул фильтров которые вы можете задать, соответсвенно фильтров может быть несколько внутри одной job
а теперь к настройке:

<желательно> в папке job создать файл с новым job  классом.
job должен наследовать 2 класса 

 1) RootJob
 2) AbstractJob
 обязательные методы:
 
 * handle - метод-команда работник, отвечает за основную работу job (наследован от RootJob)
 * run_filters - метод-команда, выполняющий логику запуска фильтров
 * job_description - метод-запрос возвращающий описание Job
 
 необязательные методы - любые методы в т.ч ваши фильтры обработчики
 

более подробно о JOB можно узнать в default_job, там реализован уже готовые реализации JOB, по ним можно добавить новые JOB. 

далее в файле configs/config.py нужно импортировать вашу новую Job и добавить ее в JOB_SET словарь 
желательный вид такой: job_name:job


1) легко описать новые JOB при работе с программой
2) соблюден принцип open/closed (не надо лезть в main.py и что-то переписывать)
3) простота расширения
4) теперь dataset обернут в объект, что дает некоторые преимущества(к примеру вы можете описать некоторые методы работы с датасетом)
