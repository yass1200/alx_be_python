class BankAccount:
    """A simple BankAccount class to demonstrate basic OOP concepts."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount if funds are sufficient.
        Return True if successful, otherwise False.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance formatted to two decimals."""
        print(f"Current Balance: ${self.account_balance:.2f}")
