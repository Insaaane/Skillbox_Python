#Задача 2. Карма

import random


class KillError(Exception):
    @staticmethod
    def get_cause():
        return "Kill!"


class DrunkError(Exception):
    @staticmethod
    def get_cause():
        return "Drunk!"


class CarCrashError(Exception):
    @staticmethod
    def get_cause():
        return "Car crash!"


class GluttonyError(Exception):
    @staticmethod
    def get_cause():
        return "Gluttony!"


class DepressionError(Exception):
    @staticmethod
    def get_cause():
        return "Depression"


def one_day():
    _karma = random.randint(1, 7)
    if random.randint(1, 10) == 10:
        exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        exception = random.choice(exceptions)
        raise exception()
    return _karma


karma = 0
while karma < 500:
    try:
        karma += one_day()
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
        with open('karma.log', 'a') as karma_log:
            karma_log.write(e.get_cause() + "\n")

karma_log.close()
