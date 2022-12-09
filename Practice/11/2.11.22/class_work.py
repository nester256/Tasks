from random import randint
from typing import List


class Car:
    def __init__(self, speed: int, name):
        self.speed = speed
        self.name = name

\
class Race:
    def __init__(self, cars: List[Car], laps: int, lap_distance: int):
        self.cars = cars
        self.laps = laps
        self.lap_distance = lap_distance

    def race(self):
        cars_count = len(self.cars)
        results = {car.name: 0 for car in self.cars}
        for lap in range(self.laps):
            crashed_car = self.cars.pop(randint(0, cars_count - 1))
            results[crashed_car.name] = -1
            for car in self.cars:
                if cars_count > lap:
                    results[car.name] = self.lap_distance / car.speed
        return results


car_1 = Car(90, 'toyota_supra')
car_2 = Car(110, 'nissan cefiro')
car_3 = Car(84, 'zhiguly')

zmeinka = Race([car_1, car_2, car_3], 4, 200)
print(zmeinka.race())
