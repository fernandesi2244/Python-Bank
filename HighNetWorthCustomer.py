from Customer import Customer

class HighNetWorthCustomer(Customer):
    'Represents a high net worth customer of a bank'
    def __init__(self, name, age, income, acct, preferredInvestment, birthday):
        super().__init__(name, age, income, acct)
        self.preferredInvestment = preferredInvestment
        self.birthday = birthday
    
    def changePreferredInvestment(self, newPreferredInvestment):
        oldChoice = self.preferredInvestment
        self.preferredInvestment = newPreferredInvestment
        return oldChoice