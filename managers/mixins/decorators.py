from functools import wraps
import sys


def exception_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f'[ERROR] Произошла ошибка в методе {func.__name__}. Код ошибки:')
            print(str(exc))
            print('Возможно ошибка в некоректном json файле проверьте ваш json\nВыход')
            sys.exit(0)
        return result

    return wrapper


def job_exception_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            class_job = func(*args, **kwargs)
        except Exception as exc:
            print(f'[ERROR] Произошла ошибка в JOB {args[0].__class__.__name__}. Код ошибки:')
            print(str(exc))
            print('Выход')
            sys.exit(0)
        return class_job
    return wrapper
