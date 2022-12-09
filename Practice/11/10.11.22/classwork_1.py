class Mixin_levels:
    levels = ["junior", "middle", "senior"]

    def __init__(self, level):
        self.__level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def check(self, level):
        if level in Mixin_levels.levels:
            self.__level = level
        else:
            raise Exception("Неправильно задан уровень")


class Task(Mixin_levels):

    def __init__(self, title, level):
        super().__init__(level)
        self.title = title


class Employee(Mixin_levels):

    def __init__(self, name, level, department, skill=0):
        self.name = name
        super().__init__(level)
        self.department = department
        self.__tasks = []
        self.skill = skill

    def get_task(self, task: Task):
        levels = super().levels
        if levels.index(self.level) >= levels.index(task.level):
            self.__tasks.append(task)
        else:
            print("уволен")

    def do_task(self, title):
        for i in range(len(self.__tasks)):
            if title == self.__tasks[i].title:
                self.__tasks.pop(i)
                print(f"Задача {title} выполнена")
                self.skill += 1
                break
        else:
            print("Задача не найдена")


emp = Employee("вася", "junior", "Балтика")
task = Task("убрать весь легаси", "junior")
emp.get_task(task)
emp.do_task("убрать весь легаси")
print(emp.skill)