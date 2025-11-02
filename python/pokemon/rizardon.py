class Pokemon:
    def __init__(self):
        self.name = "リザードン"
        self.type1 = "ほのお"
        self.type2 = "ひこう"
        self.hp = 100


    def attack(self):
        pokemon_attack = f"{self.name}のこうげき!"
        return pokemon_attack


poke = Pokemon()

print(poke.attack())