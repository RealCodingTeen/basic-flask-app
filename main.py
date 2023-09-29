import random

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.accounts = []

    def create_account(self, account_type, initial_balance):
        account = Account(account_type, initial_balance)
        self.accounts.append(account)
        return account

class Account:
    def __init__(self, account_type, balance):
        self.account_number = random.randint(10000, 99999)
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

class Transaction:
    @staticmethod
    def transfer(sender, receiver, amount):
        if amount > 0 and amount <= sender.balance:
            sender.balance -= amount
            receiver.balance += amount
            return f"Transferred ${amount} from {sender.account_number} to {receiver.account_number}"
        else:
            return "Invalid transfer amount or insufficient funds."

def main():
    customer1 = Customer("John Doe", "123 Main St", "555-555-5555")
    customer2 = Customer("Jane Smith", "456 Oak St", "555-123-4567")

    account1 = customer1.create_account("Savings", 1000)
    account2 = customer2.create_account("Checking", 500)

    print(f"{customer1.name}'s Accounts:")
    for account in customer1.accounts:
        print(f"Account Number: {account.account_number}, Type: {account.account_type}, Balance: ${account.balance}")

    print(f"{customer2.name}'s Accounts:")
    for account in customer2.accounts:
        print(f"Account Number: {account.account_number}, Type: {account.account_type}, Balance: ${account.balance}")

    print(Transaction.transfer(account1, account2, 200))
    print(Transaction.transfer(account2, account1, 100))

if __name__ == "__main__":
    main()
