class Human:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname


class Student(Human):
    def __init__(self, name: str, speciality: str) -> None:
        pass


class Teacher(Human):
    def __init__(self):
        pass

