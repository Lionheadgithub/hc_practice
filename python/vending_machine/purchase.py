class Suica:
    def __init__(self):
        self._balance = 500

    def get_balance(self):
        return self._balance

    def charge(self, amount):
        if amount < 100:
            raise Exception("100円未満はチャージできません")
        self._balance += amount

    def pay(self, amount):
        if self._balance < amount:
            raise Exception("チャージ残高が不足しています!")
        self._balance -= amount


class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
      return f"{self.name}({self.price}円)"


class VendingMachine:
    def __init__(self):
        self.drink_list = []
        self._sales = 0

    def add_juice(self):
        for _ in range(5):
            another = Juice("ペプシ", 150)
            self.drink_list.append(another)

    def get_stock(self):
        return self.drink_list

    def buy_decision(self, juice, suica):
        found = False
        for beverage in self.drink_list:
            if beverage.name == juice.name and beverage.price == juice.price:
                found = True
                break
        enough_money = suica.get_balance() >= juice.price
        return found, enough_money

    def reduce_stock(self, juice):
        for stock in self.drink_list:
            if stock.name == juice.name and stock.price == juice.price:
                self.drink_list.remove(stock)
                return self.drink_list
        raise Exception("在庫がありません: ペプシ150 !")

    def buy_process(self, juice, suica):
        self.reduce_stock(juice)
        suica.pay(juice.price)
        self._sales += juice.price

    def get_sales_amount(self):
        return self._sales

suica = Suica()
pepsi = Juice("ペプシ", 150)
drink = VendingMachine()

drink.add_juice()
print(drink.get_stock())
print(drink.buy_decision(pepsi, suica))

drink.buy_process(pepsi, suica)
print(drink.get_stock())
print(suica.get_balance())
print(drink.get_sales_amount())