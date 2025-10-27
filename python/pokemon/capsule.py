from abc import ABC, abstractmethod

class NameService(ABC):
    @abstractmethod
    def change_name(self, new_name):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Pokemon(NameService):
    def __init__(self, name, type1, type2, hp):
        self.__name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        pokemon_attack = f"{self.__name}のこうげき!"
        return pokemon_attack

    def change_name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    def get_name(self):
        return self.__name


class Pikachu(Pokemon):
    def attack(self):
        parent_attack = super().attack()
        pikachu_attack = f"{self.get_name()}の10万ボルト!"
        return parent_attack + "\n" + pikachu_attack


class Player(NameService):
    def __init__(self):
        self.__name = ""

    def change_name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    def get_name(self):
        return self.__name


poke = Pikachu("ピカチュウ", "でんき", "かみなり", 200)

poke.change_name("ピカチュウ")
print(poke.attack())
print(poke.get_name())


poke.change_name("うんこ")
print(poke.get_name())
