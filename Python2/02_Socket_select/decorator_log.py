from functools import wraps


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " была исполнена"
            print(log_string)
            # открываем log файл и записываем данные
            with open(logfile, 'a') as opened_file:
                # Записываем логи в конкретный файл
                opened_file.write(log_string + '\n')

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='func2.log')
def func2():
    pass

func2()