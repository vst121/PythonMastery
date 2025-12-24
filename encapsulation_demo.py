class BankAccount:
    """
    A class demonstrating encapsulation in Python.
    Private attributes are prefixed with underscores.
    """

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public attribute
        self._balance = initial_balance  # Protected attribute (single underscore)
        self.__account_number = self._generate_account_number()  # Private attribute (double underscore)

    def _generate_account_number(self):
        """Private method to generate a mock account number."""
        import random
        return f"ACC{random.randint(10000, 99999)}"

    @property
    def balance(self):
        """Getter for balance - controlled access to private data."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    @property
    def account_number(self):
        """Getter for account number - read-only property."""
        return self.__account_number

    def deposit(self, amount):
        """Public method to deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")

    def withdraw(self, amount):
        """Public method to withdraw money with validation."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self._balance}")

    def get_account_info(self):
        """Public method providing controlled access to account information."""
        return {
            "holder": self.account_holder,
            "balance": self._balance,
            "account_number": self.__account_number
        }

class Employee:
    """
    Another example showing encapsulation with validation.
    """

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    @property
    def salary(self):
        """Getter for salary."""
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        """Setter with validation for salary changes."""
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        if new_salary < self.__salary * 0.9:  # Prevent large decreases
            raise ValueError("Salary decrease cannot exceed 10%")
        self.__salary = new_salary
        print(f"Salary updated to ${self.__salary}")

    def give_raise(self, percentage):
        """Public method to give a raise."""
        if percentage <= 0:
            raise ValueError("Raise percentage must be positive")
        new_salary = self.__salary * (1 + percentage / 100)
        self.salary = new_salary  # Uses the setter for validation

if __name__ == "__main__":
    print("Demonstrating Encapsulation in Python:")
    print("=" * 50)

    # BankAccount example
    account = BankAccount("Alice Johnson", 1000)
    print(f"Account created for: {account.account_holder}")
    print(f"Initial balance: ${account.balance}")  # Using property
    print(f"Account number: {account.account_number}")  # Read-only property

    account.deposit(500)
    account.withdraw(200)

    try:
        account.withdraw(2000)  # Should fail
    except ValueError as e:
        print(f"Error: {e}")

    # Direct access to private attribute (not recommended)
    print(f"Direct access to _balance: ${account._balance}")
    print(f"Direct access to __account_number: {account._BankAccount__account_number}")  # Name mangling

    print("\nAccount info via public method:")
    info = account.get_account_info()
    for key, value in info.items():
        print(f"  {key}: {value}")

    print("\nEmployee Example:")
    emp = Employee("Bob Smith", 50000)
    print(f"Employee: {emp.name}, Salary: ${emp.salary}")

    emp.give_raise(5)
    print(f"After 5% raise: ${emp.salary}")

    try:
        emp.salary = -1000  # Should fail due to setter validation
    except ValueError as e:
        print(f"Error setting salary: {e}")

    print("\nEncapsulation protects data integrity and provides controlled access,")
    print("essential for building robust and maintainable software systems.")