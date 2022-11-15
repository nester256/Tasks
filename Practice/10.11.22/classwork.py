class Dot:
    def __new__(cls, *args, **kwargs):
        print("Был вызван new")
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Был вызван init")

    def __str__(self):
        return "x = {0},  y = {1}".format(self.x, self.y)

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __truediv__(self, other):
        raise Exception("I don't know 🙁 ")

    def __pos__(self):
        return Dot(abs(self.x), abs(self.y))

    def __neg__(self):
        return Dot(abs(self.x) * -1, abs(self.y) * -1)


dot1 = Dot(1, 1)
dot2 = Dot(2, 3)
dot3 = Dot(-1, -1)
print(dot1 + dot2)
print(dot2 * dot1)
print(-dot3)
