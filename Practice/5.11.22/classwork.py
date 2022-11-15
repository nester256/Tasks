from typing import List


class Vehicle:
    def __init__(self, seats: int, speed: int):
        self.seats = seats
        self.speed = speed


class Car(Vehicle):
    def __init__(self, manf: str, model: str, seats: int, speed: int):
        super().__init__(seats, speed)
        self.manf = manf
        self.model = model


class Person:
    def __init__(self, name: str, age: int, location: str):
        self.name = name
        self.age = age
        self.location = location


class CatError(Exception):
    pass


class Transfer:
    def __init__(self, car: Car, users: List[Person], distance: int, location: str):
        self.car = car
        self.users = users
        self.distance = distance
        self.location = location
        if len(self.users) > self.car.seats:
            raise CatError

    def transfer(self):
        for user in self.users:
            user.location = self.location
        return round(self.distance / self.car.speed, 2)


car_1 = Car("Nissan", "Cefiro A31", 3, 120)
Yaroslav = Person("Yarik dalbaiob", 18, "Sochi")
Vladislav = Person("Vladik dolboiob", 18, "Sochi")
Nickita = Person("Nickita", 20, "Sochi")
transfer = Transfer(car_1, [Yaroslav, Vladislav, Nickita], 600, "Rostov-on-Don")
print(transfer.transfer())
