from functools import wraps
import sys

def exception_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f'Произошла ошибка в методе {func.__name__}. Код ошибки:')
            print(str(exc))
            sys.exit(0)
        return result
    return wrapper