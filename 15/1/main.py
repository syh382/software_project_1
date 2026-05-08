# 01
class BankAccount :
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance
    def display_info(self):
        return self.name, self.account, self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("잔액이 부족합니다")
    def get_balance(self):
        return self.balance
a = BankAccount("송유현", 100161743095, 100000)
print(a.display_info())
a.deposit(10000)
print(a.get_balance())
a.withdraw(10000)
print(a.get_balance())


