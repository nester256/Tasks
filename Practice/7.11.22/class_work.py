import random
from typing import List


class Location:
    def __init__(self, name, space):
        self.name = name
        self.space = space


class Cat:
    def __init__(self, location: List[Location], name, age, weight, current_location: Location, sq_area):
        self.location = location
        self.name = name
        self.age = age
        self.weight = weight
        self.current_location = current_location
        self.sq_area = sq_area
        self.change_location(current_location.name)

    def change_location(self, lol_location):

        def valid_location(location, sq_area, lol_location):
            if location.name != lol_location:
                if location.space > sq_area * 2:
                    return True
                elif location.space < sq_area / 2:
                    return True
            return False

        list_filter = list(filter((lambda x: valid_location(x, self.sq_area, lol_location)), self.location))
        self.current_location = random.choice(list_filter)

    def cat_dead(self):
        if self.age > 20:
            print('кот сдох')


box = Location("Box", 3)
chair = Location("Chair", 6)
fridge = Location("Fridge", 18)

cat_place = [box, chair, fridge]
cat = Cat(cat_place, "Chmo", 21, 21, chair, 21)
cat.cat_dead()

print(cat.current_location.name)
