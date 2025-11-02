from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        pokemon_attack = f"{self.name}のこうげき!"
        return pokemon_attack


class Pikachu(Pokemon):
    def attack(self):
        parent_attack = super().attack()
        pikachu_attack = f"{self.name}の10万ボルト!"
        return parent_attack + "\n" + pikachu_attack


class Zenigame(Pokemon):
    def attack(self):
        parent_attack = super().attack()
        zenigame_attack = f"{self.name}のみずでっぽう!"
        return parent_attack + "\n" + zenigame_attack


pika = Pikachu("ピカチュウ","でんき","カミナリ",200)
print(pika.attack())

zeni = Zenigame("ゼニガメ", "みず", "みずこうげき",200)
print(zeni.attack())

