#Задача 3. Отцы, матери и дети

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True
        self.calm = False


class Parent:
    def __init__(self, name, age, *children):
        self.name = name
        self.age = age
        self.children = []
        for child in children:
            self.add_child(child)

    def add_child(self, child: Child):
        if self.age - child.age < 16:
            raise ValueError
        self.children.append(child)

    def reassure_children(self):
        for child in self.children:
            child.calm = True

    def feed_children(self):
        for child in self.children:
            child.hungry = False