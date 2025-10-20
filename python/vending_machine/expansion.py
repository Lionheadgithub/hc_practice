class Suica:
    def __init__(self):
        self._balance = 500

    def get_balance(self):
        return self._balance

    def charge(self, amount):
        if amount < 100:
            raise Exception("100円未満はチャージできません")
        else:
            self._balance += amount

    def pay(self, amount):
        if self._balance < amount:
            raise Exception("チャージ残高が不足しています!")
        else:
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

    def add_juice(self, juice, count):
        for _ in range(count):
            self.drink_list.append(Juice(juice.name, juice.price))

    def get_stock(self):
        stock_dict = {}
        for juice in self.drink_list:
            key = (juice.name, juice.price)
            if key in stock_dict:
                stock_dict[key] += 1
            else:
                stock_dict[key] = 1
        stock_list = [f"{name}({price}円): {count}本" for (name, price), count in stock_dict.items()]
        return "\n".join(stock_list)

    def buy_decision(self, juice, suica):
        stock_judge = False
        money_judge = False
        for beverage in self.drink_list:
            if beverage.name == juice.name and beverage.price == juice.price:
                stock_judge = True
                break
        if suica.get_balance() >= juice.price:
            money_judge = True
        return stock_judge, money_judge

    def reduce_stock(self, juice):
        for stock in self.drink_list:
            if stock.name == juice.name and stock.price == juice.price:
                self.drink_list.remove(stock)
                return
        raise Exception("ジュースは在庫切れです")

    def buy(self, juice, suica):
        stock_judge, money_judge = self.buy_decision(juice, suica)
        if not stock_judge:
            raise Exception("ジュースは在庫切れです")
        if not money_judge:
            raise Exception("チャージ残高が不足しています")
        
        self.reduce_stock(juice)
        suica.pay(juice.price)
        self._sales += juice.price

    def get_sales_amount(self):
        return self._sales


suica = Suica()
pepsi = Juice("ペプシ", 150)
monster = Juice("モンスター", 230)
irohasu = Juice("いろはす", 120)
drink = VendingMachine()

drink.add_juice(pepsi, 5)
drink.add_juice(monster, 5)
drink.add_juice(irohasu, 5)

print(drink.get_stock())
drink.buy_decision(irohasu, suica)
drink.buy_process(irohasu, suica)
print(suica.get_balance())
print(drink.get_sales_amount())