# #bank account with class definition
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit & Withdrawal Machine!")
        
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Amount Deposited: ",amount)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient balance ")

    def display(self):
        print("Net Available Balance=",self.balance)
#creating an object of class
Joyce_Account = Bank_Account()

#calling functions with that class
Joyce_Account.deposit()
Joyce_Account.withdraw()
Joyce_Account.display()