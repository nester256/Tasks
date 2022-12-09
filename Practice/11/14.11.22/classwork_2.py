class Identifier:
    __count = 0

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def new(cls) -> object:
        cls.__count += 1
        return cls(cls.__count)

    def __str__(self):
        return "id {0}".format(self.value)


obj = Identifier.new()
print(obj)
