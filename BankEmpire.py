class BankEmpire(object):
    'Represents a collection of banks'
    def __init__(self, name, banks = []):
        self.name = name
        self.banks = banks

    def addBank(self, bank):
        if bank not in self.banks:
            self.banks.append(bank)
            return True
        else:
            print('Bank already within empire!')
        return False

    def removeBank(self, bank=None, bankName=None):
        changed = False
        if bank is not None:
            for currentBank in self.banks:
                if currentBank == bank:
                    self.banks.remove(currentBank)
                    changed = True
            print('Bank successfully removed!' if changed else 'Bank not located!')
        elif bankName is not None:
            for currentBank in self.banks:
                if currentBank.name == bankName:
                    self.banks.remove(currentBank)
                    changed = True
            print('Bank successfully removed!' if changed else 'Bank name not found!')
        else:
            print('You need to provide either a bank or bank name!')
        return changed