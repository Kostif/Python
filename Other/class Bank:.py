class Bank:

    def __init__ (self,owner,balance=0):

        self.owner=owner
        self.balance=balance

    def __str__(self):
        return f"Owner: {self.owner} , Balance: {self.balance}"
    
    def deposit(self,amount):
        
        self.balance = self.balance + amount

        return ("Hey {}, you have deposited {} to your balance. Your balance is now {}.".format(self.owner,amount,self.balance))
        
    def withdraw(self,amount):

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Hey {}, you have withdrawn {} from your balance. Your balance is now {}.".format(self.owner,amount,self.balance))
        else:
            print("Not enough money.")

acct1 = Bank('Jose',300)
acct2 = Bank('Kostas',10)

print(acct1)