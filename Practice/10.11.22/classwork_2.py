class Colour:
    def __init__(self, r, g, b, o) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.o = o

    def set_colour(self, colour, value):
        if value > 255:
            value = 255
        elif value < 0:
            value = 0

    def __add__(self, other):
        temp = Colour(0, 0, 0, 0)
        temp.set_colour("red", self.r * self.o + other.r * self.o)
        temp.set_colour("green", self.g * self.o + other.g * self.o)
        temp.set_colour("blue", self.b * self.o + other.b * self.o)
        return Colour()