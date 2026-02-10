# Parent class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")


# Child class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: ₹{interest}")


# Child class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn ₹{amount} (Overdraft allowed)")
        else:
            print("Overdraft limit exceeded")


# Testing SavingsAccount
print("---- Savings Account ----")
savings = SavingsAccount("Alice", 10000, 5)
savings.display_balance()
savings.deposit(2000)
savings.add_interest()
savings.withdraw(3000)
savings.display_balance()

# Testing CurrentAccount
print("\n---- Current Account ----")
current = CurrentAccount("Bob", 5000, 3000)
current.display_balance()
current.withdraw_with_overdraft(7000)
current.display_balance()
current.withdraw_with_overdraft(2000)
