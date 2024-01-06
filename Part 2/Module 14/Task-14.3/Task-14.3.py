#Задача 3. Логирование

import datetime
import functools
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            print(f"{func.__name__}\n{func.__doc__}")
            return func(*args, **kwargs)
        except Exception as ex:
            with open("function_errors.log", "a", encoding="UTF-8") as log:
                log.write(f"[{datetime.datetime.now()}] -- Ошибка в {func.__name__} : {ex}\n")
    return wrapper


@logging
def func_without_exceptions() -> None:
    """ Документация для func_without_exceptions """
    print("Без ошибок...")


@logging
def func_with_exception() -> None:
    """ Документация для func_with_exception """
    print("Генерация исключения...")
    raise Exception("Что-то идет не так!")


@logging
def func_with_exception_two() -> None:
    """Документация для func_with_exception_two """
    print("Генерация исключения...")
    raise Exception("Что-то идет не так 2!")


func_without_exceptions()
print()
func_with_exception()
print()
func_with_exception_two()