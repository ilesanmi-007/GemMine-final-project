#ATM CLASS
#default amount== 1k
#methods: withdraw, add money, check balance
class ATM:
    def __init__(self, cash = 1000):
        self.cash = cash

    def check_balance(self):
        print (self.cash)

    def add_money(self, newmoney):
        self.cash = self.cash + newmoney

    def withraw(self, amount):
        self.cash = self.cash - amount
