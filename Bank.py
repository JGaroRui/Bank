class Bank:
    def __init__(self,bankaccount):
        self.bankaccount = bankaccount
        self.balance=0
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance = self.balance - amount
        else:
            print("You don't have enough balance")
        return self.balance
    def getbalance(self):
        return self.balance
    def __str__(self):
        return self.bankaccount
