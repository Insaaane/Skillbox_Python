#Задача 2. Замедление кода

import functools
import time
from typing import Callable, Any


def delay_execution(seconds: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@delay_execution(seconds=3)
def some_function():
    print("Сделано!")


print("Выполним какую-то функцию...")
some_function()
