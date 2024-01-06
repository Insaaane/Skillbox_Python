#Задача 2. Математический модуль

import math


class MyMath:
    @classmethod
    def circle_len(cls: 'MyMath', radius: float) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls: 'MyMath', radius: float) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls: 'MyMath', side_len: float) -> float:
        return side_len ** 3

    @classmethod
    def sphere_surface_area(cls: 'MyMath', radius: float) -> float:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
