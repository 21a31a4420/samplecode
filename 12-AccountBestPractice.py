from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,accnum,customername,acctype,balance):
        self.accno=accnum
        self.customername=customername
        self.acctype=acctype
        self.balance=balance
    
    def __str__(self):
        return "acc num:{}\nCustomerName:{}\nAccounttype:{}\nBalance:{}\n".format(self.accno,self.customername,self.acctype,self.balance)
    
    def deposit(self,amount):
        self.balance+=amount
    @abstractmethod
    def withdraw(self,amount):pass
class Savingaccount(Account):
    def withdraw(self, amount):
        if (self.balance-amount<500):
            raise Exception("balance amount is lesser than rs.500")
        else:
            self.balance-=amount
class CurrentAccount(Account):
    def withdraw(self, amount):
        self.balance-=amount
sa=Savingaccount(101,'san','savings',15000)
print(sa)
amount=float(input('enter amount to be withdrawn:'))
sa.withdraw(amount)
print('current balance:',sa.balance)

ca=Savingaccount(102,'sannn','current',15000)
print(ca)
amount=float(input('enter amount to be withdrawn:'))
ca.withdraw(amount)
print('current balance:',ca.balance)

