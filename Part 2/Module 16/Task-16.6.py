#Задача 6. Класс-декоратор

import time
import functools
from typing import Callable, Any


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs) -> Any:
        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")

        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Результат: {result}")
        print(f"Время выполнения: {execution_time} секунд")

        return result


@LoggerDecorator
def complex_algorithm(arg1, arg2) -> Any:
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            result += i + j
    return result


result = complex_algorithm(10, 5000)
