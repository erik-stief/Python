from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def __init__(self, account_number, account_holder_name, balance=0):
        pass
    @abstractmethod
    def deposit(self, account_number, account_holder_name):
        pass
    @abstractmethod
    def withdraw(self, account_number, account_holder_name):
        pass
    @abstractmethod
    def display_balance(self, account_number, account_holder_name):
        pass

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, account_number, account_holder_name):
        self.balance += float(input("Please enter your deposit amount: "))
    def withdraw(self, account_number, account_holder_name):
        self.balance -= float(input("Please enter your withdraw amount: "))
    def display_balance(self, account_number, account_holder_name):
        print(f"Your current balance is: {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, account_number, account_holder_name):
        self.balance += float(input("Please enter your deposit amount: "))
    def withdraw(self, account_number, account_holder_name):
        self.balance -= float(input("Please enter your withdraw amount: "))
    def display_balance(self, account_number, account_holder_name):
        print(f"Your current balance is: {self.balance}")

