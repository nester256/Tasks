class Square:
    def __init__(self, side: float) -> None:
        self.side = side


class Rectangle:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    @classmethod
    def from_square(cls, square: Square) -> object:
        return cls(square.side, square.side)

    def __str__(self):
        return 'a: {0}, b: {1}'.format(self.a, self.b)


sq = Square(3)
n_rc = Rectangle.from_square(sq)
print(n_rc)
