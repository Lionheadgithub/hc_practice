class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        pokemon_attack = f"{self.name}のこうげき!"
        return pokemon_attack


if __name__ == "__main__":
    poke = Pokemon("ピカチュウ","でんき", "カミナリ", 200)
    print(poke.attack())