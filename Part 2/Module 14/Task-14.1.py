#Задача 1. Как дела?

import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func(*args, **kwargs)
    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
