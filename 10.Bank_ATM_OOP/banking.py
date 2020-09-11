# bank statement - hesap ekstresi
    # current account - cari hesap
    #deposit - para yatırmak
    #withdraw - para çekme
    #overdrawn - limit fazlası
    #transfer 
from customer import Customer

class Banking(Customer):
    def __init__(self, account_number, first_name, last_name, password):
        super().__init__(account_number, first_name, last_name, password)

    
    def withraw(self, money):
        if money > self._balance:
            print(f'overdrawn\nYou can maximum {self._balance} withdraw ')
        else:
            self._balance -= money
            return self._balance

    
    def transfer(self, money):
        pass
    
    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, money):       #object.balance = value
        self._balance += money
        return self._balance

