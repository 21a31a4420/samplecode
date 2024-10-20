accountno=input('Enter acc num:')
customername=input('enter customer name:')
accounttype=input('Enter acc type:')
balance=float(input('enter balance:'))

def showacc():
    print('acc#:{}\nCustomername:{}\nAcc type:{}\nBalance:{}\n'.format(accountno,customername,accounttype,balance))

def withdraw(balance,amount):
    if accounttype=='SAVINGS':
        newbalance=balance-amount
        if newbalance < 500:
            raise Exception('Insufficient balance,cant withdraw amount')
        else:
            balance =newbalance
            return balance
    elif accounttype == 'CURRENT':
        balance=balance - amount
        return balance
showacc()
amount =float(input('enter amount to be withdrawn:'))
balance =withdraw(balance,amount)
print('after withdraw new balance:')
print('balance:',balance)