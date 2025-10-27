from pokemon_main import Pokemon

class Pikachu(Pokemon):
    def __init__(self, _name, _type1, _type2, _hp):
        super().__init__(_name, _type1, _type2, _hp)

    def attack(self):
        parent_attack = super().attack()
        pokemon_attack = f"{self.name}の10万ボルト!"
        return parent_attack + "\n" + pokemon_attack


pika = Pikachu("ピカチュウ","でんき","カミナリ",200)
print(pika.attack())