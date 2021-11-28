[WINDOWS] python main.py

[OS X / LINUX] python3 main.py

Помимо фильтров вы можете так же писать кастомные JOBS(задачи, работы)
к примеру: проход по всем фильтрам это всего лишь одна JOB, (посмотрите  файл jobs/default_job)
а теперь к настройке:

<желательно> в папке job создать файл с новым job  классом.
job должен наследовать 2 класса 

 1) RootJob
 2) AbstractJob
 
 пример job
```python
class AddJob(RootJob, AbstractJob):
    @job_exception_output
    def handle(self):
        self.add_in_dataset()
        super().handle()

    def add_in_dataset(self):
        self.dataset_object.dataset['name'] = 100

    def job_description(self):
        return f'эта JOB которая создает поле name и ложит туда 100'
```
handle - это метод работник, здесь переопределяется метод handle от RootJob, здесь происходит вся работа. после ее выполнения не забудьте вызвать super().handler(), таким образом вы отдадите указание на выполнение следующей job 

* Это важный параметр

так же с абстрактного класса подтягивается метод job_description, этот метод просто возвращает описание вашей job.

пример job
```python
 def job_description(self):
    return f'эта JOB предназначена для прохода json файла по фильтрам.\nПоставлены фильтры: {self.get_filters_name()}'
```
* Это важный параметр

более подробно о фильтах можно узнать в default_job, там реализован готовый фильтр, по нему можно добавить новые JOB. 

далее в файле configs/config.py нужно импортировать вашу новую Job и добавить ее в JOB_SET словарь 
желательный вид такой: job_name:job


[WARNING] - этот способ медленнее способа описанного в ветке (main). Но он дает кучу преимуществ
1) легко описать новые JOB при работе с программой
2) соблюден принцип open/closed (не надо лезть в main.py и что-то переписывать)
3) простота расширения
4) теперь dataset обернут в объект, что дает некоторые преимущества(к примеру вы можете описать некоторые методы работы с датасетом)
5) скорость упала не критически(накладные расходы на создание объекта и цепочки JOB)


Формат фильтров. Стандартные фильтры располагаются в filters/filter.py, кастомные фильтры желательно располагать в той же директории(filter). Далее их нужно импортировать в configs/config.py и добавить в FILTER_SET. настройка порядка обхода там же

фильтры на вход должны принимать обьект типа dict и возвращать его же, то есть:
```python
def <your_filter_name>(data:dict) -> dict: ...
```
