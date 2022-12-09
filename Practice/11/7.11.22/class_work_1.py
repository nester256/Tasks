from typing import List


class Flour:
    def __init__(self, name: str, category) -> None:
        self.name = name
        self.category = category


class Filling:
    def __init__(self, name: str, sweet=True) -> None:
        self.name = name
        self.sweet = sweet


class Eggs:
    def __init__(self, category, name):
        self.category = category
        self.name = name


rice_flour = Flour("экстра", "рисовая")
jam = Filling("Абрикосовый джем")
egg = Eggs("С0", "Куриное")


class PieAggregation:
    def __init__(self, flour: Flour, filling: Filling, eggs: List[Eggs]) -> None:
        self.flour = flour
        self.filling = filling
        self.eggs = eggs


class PieComposition:
    def __init__(self, flour_type, filling_type):
        self.flour = Flour(flour_type, "Высший сорт")
        self.filling = Filling(filling_type, sweet=True)
        self.eggs = [Eggs("Куриное", "C0")] * 2
