import json
from typing import List


class Wheel:
    def __init__(self, mark, diameter):
        self.mark = mark
        self.diameter = diameter

class Engine:
    def __init__(self, mark, volume, hp):
        self.mark = mark
        self.volume = volume
        self.hp = hp

class Car:
    def __init__(self, manf: str, name: str, body: str, on_the_go: bool, wheels: List[dict], engine: dict):
        self.manf = manf
        self.name = name
        self.body = body
        self.on_the_go = on_the_go
        self.engine = Engine(**engine) if engine else None
        self.wheels = [Wheel(**wheel) for wheel in wheels] if wheels else None

    def __str__(self):
        data = self.__dict__
        return "\n".join(["{0} : {1}".format(key, data[key]) for key in data])

    def to_dict(self):
        result = self.__dict__
        result["wheels"] = [wheel.__dict__ for wheel in self.wheels]
        result["engine"] = self.engine.__dict__
        return result

# with open("cars.json", "rt") as file:
#     data = file.read()
#     car = json.loads(data)
#     new_car = [Car(**car) for car in json.loads(data)["cars"]]
#     print(*new_car)

with open("bmw.json", "rt") as file:
    data = file.read()
    car = json.loads(data)
    bmw = Car(**car)


with open("bmw_serialized.json", "wt") as file:
    file.write(json.dumps(bmw.to_dict()))