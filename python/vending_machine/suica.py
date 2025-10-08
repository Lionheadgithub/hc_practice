class Suica:
    def __init__(self):
        self._balance = 500

    def get_balance(self):
        return self._balance

    def charge(self, amount):
        if amount < 100:
            raise Exception("100円未満はチャージできません")
        self._balance += amount


suica = Suica()
suica.charge(200)
print(suica.get_balance())