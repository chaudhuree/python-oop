from abc import ABC, abstractmethod
from random import randint
from art import *

Art = text2art("Save Money")
print(Art)


class Account(ABC):
    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.savingAccounts = {}
        # [key][0] => name ; [key][1] => balance

    def createAccount(self, name, deposit):
        print()
        self.accountNumber = randint(10000, 99999)
        print('your account creation has been successful.')
        print(f"your account name is: {name} and your,")
        print('your account number is :', self.accountNumber)
        self.savingAccounts[self.accountNumber] = [name, deposit]
        print()

    def authenticate(self, name, accountNumber):
        print()
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("account authentication completed..")
                self.accountNumber = accountNumber
                print()
                return True

    def withdraw(self, withdrawlAmmount):
        print()
        self.savingAccounts[self.accountNumber][1] -= withdrawlAmmount
        print("withdraw successful: ")
        self.displayBalance()
        print()

    def deposit(self, depositAmmount):
        self.savingAccounts[self.accountNumber][1] += depositAmmount
        self.displayBalance()
        pass

    def displayBalance(self):
        print('your current balance is: ', self.savingAccounts[self.accountNumber][1])


savingsAccount = SavingsAccount()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    print()
    if userChoice == 1:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
        print()
    elif userChoice == 2:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        print()
        if authenticationStatus == True:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avialable balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                print()
                if userChoice == 1:
                    print()
                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                    print()
                elif userChoice == 2:
                    print()
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                    print()
                elif userChoice == 3:
                    print()
                    savingsAccount.displayBalance()
                    print()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
        quit()
