import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        # self.transaction_list = [(Account._current_time(), balance)]
        print("*" * 150)
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than zero and no more than your account balance")
            self.show_balance()

    def show_balance(self):
        print("Balance is: {} ".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":

    josh = Account("Joshua", 0)
    print("*" * 150)

    josh.deposit(1000)

    print("*" * 150)

    josh.withdraw(1500)
    josh.withdraw(500)

    josh.show_transactions()

    print("*" * 150)
    print("*" * 150)

    steph = Account("Stephen", 800)
    print("*" * 150)

    steph.deposit(100)
    print("*" * 150)

    steph.withdraw(1200)
    steph.withdraw(200)
    steph.__balance = 1700
    steph.show_balance()
    print("*" * 150)

    steph.show_transactions()
