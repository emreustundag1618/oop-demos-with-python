class BankAccount:
    
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    

account = BankAccount("Emre Ustundag")
    
account.deposit(1500)
print(account.balance)
account.withdraw(1000)
print(account.balance)