from typing import List


class RectangleError(Exception):
    def __init__(self):
        print("Ашипка")


class Rectangle:
    def __init__(self, sides: List[float]) -> None:
        self.sides = sides
        if not self.is_valid():
            raise RectangleError

    def is_valid(self) -> bool:
        if len(self.sides) != 4 or len(set(self.sides)) >= 2:
            for side in self.sides:
                if not isinstance(side, (int, float)):
                    return False
                if side <= 0:
                    return False
        return True


rec = Rectangle([2, 3, 3, -1])
