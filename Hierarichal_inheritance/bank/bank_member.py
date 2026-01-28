# Hierarchical Inheritance Example - Bank System

# Parent class
class Bank:
    def bank_info(self):
        print("Welcome to ABC Bank!")
        print("We offer various types of accounts.\n")

# Child class 1
class SavingsAccount(Bank):
    def account_info(self):
        print("This is a Savings Account.")
        print("Interest Rate: 4% per annum\n")

# Child class 2
class CurrentAccount(Bank):
    def account_info(self):
        print("This is a Current Account.")
        print("No interest is provided on current accounts.\n")

# Child class 3
class FixedDeposit(Bank):
    def account_info(self):
        print("This is a Fixed Deposit Account.")
        print("Interest Rate: 7% per annum\n")

# Creating objects of each subclass
savings = SavingsAccount()
current = CurrentAccount()
fixed = FixedDeposit()

# Calling methods
savings.bank_info()
savings.account_info()

current.bank_info()
current.account_info()

fixed.bank_info()
fixed.account_info()