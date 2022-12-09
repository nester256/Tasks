# Тут будем работать с json
import json

def parse_car(car: any, level: int = 0):
    padding = "\t" * level
    if isinstance(car, dict):
        for key in car.keys():
            print("{0} {1}: {2}".format(padding, key, type(key)))
            value = car[key]
            parse_car(value, level + 1)
    elif isinstance(car, list):
        for subvalue in car:
            print("{0} {1:-^10}".format(padding, '-'))
            parse_car(subvalue, level+1)
    else:
        print("{0} {1}: type:{2}".format(padding, car, type(car)))


with open("bmw.json", "rt") as file:
    data = file.read()
    none = json.loads(data)

parse_car(none)