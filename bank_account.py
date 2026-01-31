class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. Current Balance: {self.__balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        if amount > 0:
            self.__balance -= amount
            return f"Withdrew {amount}. Current Balance: {self.__balance}"
        return "Invalid withdrawal amount"

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return f"Interest added: {interest}"


account1 = BankAccount("ACC101", "Alice", 1000)
account2 = SavingsAccount("ACC102", "Bob", 2000)

print(account1.deposit(500))
print(account1.withdraw(300))
print("Balance:", account1.get_balance())

print(account2.deposit(1000))
print(account2.add_interest())
print("Balance:", account2.get_balance())
