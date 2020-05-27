class BankAccount(object):
    'Represents a bank account that a customer can hold'

    def __init__(self, acctType='Savings', balance=0):
        self.type = acctType
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        return self.balance

    def withdraw(self, amount):
        self.balance-=amount
        return self.balance