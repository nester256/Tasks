from typing import List


class Hero:
    def __init__(self, name: str, attack_dmg: int, hp: int, armor: int):
        self.attack_dmg = attack_dmg
        self.hp = hp
        self.armor = armor
        self.name = name


class Game:
    def __init__(self, heroes: List[Hero]):
        self.heroes = heroes

    def duel(self, hero_1: Hero, hero_2: Hero):
        hp_1, hp_2 = hero_1.hp, hero_2.hp
        print("---Начало боя---")
        i = 1
        while hp_1 > 0 and hp_2 > 0:
            print("----Раунд {0}-----", format(i))
            hp_1 -= (hero_2.attack_dmg - hero_1.armor)
            hp_2 -= (hero_1.attack_dmg - hero_2.armor)
            print("*** Результаты боя ***\n"
                  "Герой 1: {0}\n"
                  "Герой 2: {1}\n".format(hp_1, hp_2))
            print("---Канец---")
            i += 1
        if hp_1 <= 0:
            print("Победил hero_2")
        elif hp_2 <= 0:
            print("Победил hero_1")
        elif hp_1 <= 0 and hp_2 <= 0:
            print("Ничья!")

    def play(self):
        for i in range(len(self.heroes)):
            print(i + 1, self.heroes[i].name)
        her1 = int(input())
        her2 = int(input())
        self.duel(self.heroes[her1 - 1], self.heroes[her2 - 1])


hero_1 = Hero("Ярик", 5, 10, 2)
hero_2 = Hero("Заугольникова", 3, 9, 1)
Game([hero_2, hero_1]).play()
