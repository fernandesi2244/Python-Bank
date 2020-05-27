class Customer(object):
    'Represents a customer of a bank'
    def __init__(self, name, age, income, acct):
        self.name = name
        self.age = age
        self.income = income
        self.bankAccount = acct
    
    def incrementAge(self, incrementValue=1):
        pastAge = self.age
        self.age+=incrementValue
        return pastAge

    def changeIncome(self, newIncome):
        pastIncome = self.income
        self.income = newIncome
        return pastIncome
    
    def changeBankAccount(self, newAccount):
        oldAcct = self.bankAccount
        self.bankAccount = newAccount
        return oldAcct

    def makeDeposit(self, amount):
        if(amount>=0):
            self.bankAccount.deposit(amount)
            print(f'Successful deposit of {amount} made!')
        else:
            print('You cannot deposit a negative amount!')
        return self.bankAccount.balance

    def makeWithdrawal(self, amount):
        balance = self.bankAccount.balance
        if(amount<0):
            print('You cannot withdraw a negative amount!')
            return balance
        if(amount>balance):
            print(f'There is not enough money in the account to withdraw ${amount}')
            return balance
        return self.bankAccount.withdraw(amount)