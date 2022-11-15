from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth(cls, name, birthday):
        return cls(name, (date.today() - birthday).days // 365)

    def __str__(self):
        return 'name: {0}, age: {1}'.format(self.name, self.age)

    @staticmethod
    def create_static(name, age):
        return Person(name, age)

    @classmethod
    def create_from_class(cls, name, age):
        return cls(name, age)


class Student(Person):
    pass


st_1 = Student.create_from_class("Petya", 12)
st_2 = Student.create_static("Ivan", 19)
print(type(st_1))
print(type(st_2))

