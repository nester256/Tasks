class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def greeting(self):
    #     print("Пруэйт Насяльника, я {0}, " \
    #           "мине {1} годов".format(self.name, self.age))


class Student(Human):
    def __init__(self, name, age, college):
        super().__init__(name, age)
        self.college = college

    def greeting(self):
        print("Пруэйт Насяльника, я {0}, " \
              "мине {1} годов, я не спать, я плитка делать в {2}".format(self.name, self.age, self.college))

    def attend_classes(self, subject):
        if self.name == "Matway" and subject == "Tennis":
            return True
        else:
            return False


Jagroslave = Student("Iroslave", 54, "ПТУ на краю света")
matwey = Student("Matwey", 20, "IT Sirius")
matwey.greeting()
Jagroslave.greeting()
print(matwey.attend_classes("Tennis"))
print(Jagroslave.attend_classes("Tennis"))

rect_1 = Rectangle(4, 2)
print("Периметр: ", rect_1.perimetr())
print("Площадь: ", rect_1.area())
