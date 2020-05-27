class Bank(object):
    'Represents a bank'

    def __init__(self, name, customers = []):
        self.name = name
        customers = Bank.noRepeats(customers)
        self.customers = customers
    
    def addCustomer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
            print('Customer successfully added!')
            return True
        else :
            print('The customer is already enrolled with the bank!')
            return False

    def removeCustomer(self, customer = None, customerName = None):
        changed = False
        if customer is not None:
            for currentCustomer in self.customers:
                if currentCustomer == customer:
                    self.customers.remove(currentCustomer)
                    changed = True
            print('Customer successfully removed!' if changed else 'Customer not located!')
        elif customerName is not None:
            for currentCustomer in self.customers:
                if currentCustomer.name == customerName:
                    self.customers.remove(currentCustomer)
                    changed = True
            print('Customer successfully removed!' if changed else 'Customer name not found!')
        else:
            print('You need to provide either a customer or a customer name!')
        return changed
    
    def __str__(self):
        return self.name

    @staticmethod
    def noRepeats(customerList):
        customerSet = set(customerList)
        return list(customerSet)