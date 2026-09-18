class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds! Current balance: ₹{self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder} | Current Balance: ₹{self.balance:.2f}")


account = BankAccount("Saurabh", 1500.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(800.0)
account.display_balance()