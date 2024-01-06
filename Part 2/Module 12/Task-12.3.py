#Задача 3. Свой словарь

class MyDict(dict):
    def get(self, __key):
        result = super().get(__key)
        if result is None:
            return 0
        else:
            return result


my_dict = MyDict()
my_dict['Ключ'] = 'Значение'

print(my_dict.get("Ключ"))
print(my_dict.get("key"))


