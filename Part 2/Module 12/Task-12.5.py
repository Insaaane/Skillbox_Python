#Задача 5. Стек

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def remove_task(self, task):
        temp_stack = Stack()
        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                temp_stack.push(current_task)
        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

    def __str__(self):
        sorted_tasks = sorted(self.tasks.items, key=lambda x: x[1])
        result = ""
        for task in sorted_tasks:
            result += f"{task[1]} — {task[0]}\n"
        return result


manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сделать ДЗ", 2)

print(manager)

manager.remove_task("сделать ДЗ")
manager.remove_task("сделать уборку ")
manager.remove_task("помыть посуду")

print(manager)
