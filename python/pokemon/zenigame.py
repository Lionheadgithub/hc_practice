from pokemon_main import Pokemon

class Zenigame(Pokemon):
    def __init__(self, _name, _type1, _type2, _hp):
        super().__init__(_name, _type1, _type2, _hp)

    def attack(self):
        parent_attack = super().attack()
        pokemon_attack = f"{self.name}のみずでっぽう!"
        return parent_attack + "\n" + pokemon_attack


zeni = Zenigame("ゼニガメ", "みず", "みずこうげき",200)
print(zeni.attack())