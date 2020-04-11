class Account:
    """ Simple account class with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("*" * 150)
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            josh.show_balance()
        else:
            print("Amount must be greater than zero and no more than your account balance")
            josh.show_balance()

    def show_balance(self):
        print("Balance is: {} ".format(self.balance))


if __name__ == "__main__":
    josh = Account("Joshua", 0)
    josh.show_balance()
    print("*" * 150)

    josh.deposit(1000)

    print("*" * 150)

    josh.withdraw(1500)
    josh.withdraw(500)

    print("*" * 150)

