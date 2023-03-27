class BankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return f'Deposit Accepted, your balance is : {self.balance}'

    def withdraw(self,amount):
        if amount>self.balance:
            return "Transaction Declined, Insufficient fund!!!"
        else:
            self.balance-=amount
            return f'Withdrawl of {amount} is successful, your balance is : {self.balance}'

    def __str__(self):
        return f'Account Owner: ,{self.owner}\nAccount Balance: ${self.balance}'


acct1 = BankAccount('Jose',100)
print(acct1)
#Show account owner
print("Account owner is: ",acct1.owner)
print("Account balance is: ",acct1.balance)

# Make a series of deposits and withdrawals
print(acct1.deposit(50))
print(acct1.withdraw(75))
# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))