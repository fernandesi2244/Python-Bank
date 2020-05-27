from BankEmpire import BankEmpire
from Bank import Bank
from Customer import Customer
from HighNetWorthCustomer import HighNetWorthCustomer
from BankAccount import BankAccount
from datetime import datetime as dt

ianbotzEmpire = BankEmpire('The Ianbotz Bank Empire')

''''''''''''''''''''''''''''''''''''''''''
iBank1 = Bank('Lavender Side Bank')

georgeCustomer = Customer('George Curious', 23, 60_000, BankAccount(balance=130))
stevenCustomer = HighNetWorthCustomer('Steven Hillborough', 78, 3_200_000, BankAccount(balance=36_000_000), 'Exchange Traded Funds', dt(1942, 3, 26))

iBank1.addCustomer(georgeCustomer)
iBank1.addCustomer(stevenCustomer)

ianbotzEmpire.addBank(iBank1)

''''''''''''''''''''''''''''''''''''''''''
iBank2 = Bank('Mason Hill Bank')

williamCustomer = Customer('William Blake', 18, 40_000, BankAccount(balance=200))
joshCustomer = Customer('Josh Maven', 35 , 80_000, BankAccount(balance=30_000))
ronaldCustomer = HighNetWorthCustomer('Ronald McDonald', 68, 128_200_000, BankAccount(balance=1_200_000_000), 'Foreign Exchange Market', dt(1950, 8, 2))

iBank2.addCustomer(williamCustomer)
iBank2.addCustomer(joshCustomer)
iBank2.addCustomer(ronaldCustomer)

ianbotzEmpire.addBank(iBank2)
''''''''''''''''''''''''''''''''''''''''''
print()

print(f'{iBank1.name} has', len(iBank1.customers), 'customers.')
print(f'{iBank2.name} has', len(iBank2.customers), 'customers.')

print()

print(f'Customers of banks in {ianbotzEmpire.name}:')
for bank in ianbotzEmpire.banks:
    print(f'Bank: {bank.name}')
    for customer in bank.customers:
        print(f' Name: {customer.name} | Age: {customer.age} | Balance:', '${:0,.2f}'.format(customer.bankAccount.balance))