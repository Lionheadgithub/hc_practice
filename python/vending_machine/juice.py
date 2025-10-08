class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        self.drink_list = []

    def add_juice(self, juice):
        for _ in range(5):
            name_price = juice.name,juice.price
            self.drink_list.append(name_price)

    def get_stock(self):
        return self.drink_list


pepsi = Juice("ペプシ", 150)
drink = VendingMachine()
drink.add_juice(pepsi)
print(drink.get_stock())