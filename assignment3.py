from datetime import datetime
import random
from abc import ABC, abstractmethod


def generate_account_number():
    available_numbers = list(range(10000,99999))
    account_number = random.choice(available_numbers)
    available_numbers.remove(account_number)
    if len(available_numbers) == 0:
        return ""
    return str(account_number)

def display_largest_account(list):
    balance_list = []
    for account in list:
        balance_list.append(account.balance)
    balance_list.sort()
    largest_balance = balance_list[-1]
    largest_accounts = ""
    for account in list:
        if account.balance == largest_balance:
            largest_accounts += account.display_info() + "\n"

    largest_accounts += "The account(s) is(are) the oldest account(s) from the list."
    return largest_accounts

def display_oldest_account(list):
    date_list = []
    for account in list:
        date_list.append(account.open_date)
    date_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
    oldest_date = date_list[0]
    oldest_accounts = ""
    for account in list:
        if account.open_date == oldest_date:
            oldest_accounts += account.display_info() + "\n"

    oldest_accounts += "The account(s) is(are) the oldest account(s) from the list."
    return oldest_accounts
class Account(ABC):
    account_number = ""
    name = ""
    open_date = ""
    balance = 0.0
    list_accounts = []

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn.\nRemaining balance: ${self.balance}"
        else:
            return f"${amount} Invalid amount.\nAvailable balance: ${self.balance}"


    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.balance += amount
        return f"${amount} deposited.\nBalance: ${self.balance}"

class SavingsAccount(Account):
    interest = 0.0
    list_savings_accounts = []

    def __init__(self, name, open_date, balance, interest):
        self.name = name
        self.open_date = open_date
        self.balance = balance
        self.interest = interest
        self.account_number = generate_account_number()
        self.list_accounts.append(self)
        self.list_savings_accounts.append(self)

    def display_info(self):
        return (f"{self.name}, your savings account number is {self.account_number}.\n"
                f"Open date: {self.open_date}\n"
                f"Interest rate: {self.interest}\n"
                f"Balance: ${self.balance}")



class CheckingAccount(Account):
    list_checking_accounts = []

    def __init__(self, name, open_date, balance):
        self.name = name
        self.open_date = open_date
        self.balance = balance
        self.account_number = generate_account_number()
        self.list_accounts.append(self)
        self.list_checking_accounts.append(self)

    def display_info(self):
        return (f"{self.name}, your savings account number is {self.account_number}.\n"
                f"Open date: {self.open_date}\n"
                f"Balance: ${self.balance}")

def main():
    s1 = SavingsAccount("Emma Smith", "2022-04-03", 550, 0.1)
    print(s1.display_info())

    c1 = CheckingAccount("Jackson Johnson", "2021-07-27", 300)
    #print(c1.display_info())

    #print(s1.withdraw(1000))

    s1.withdraw(50)

    c1.deposit(40)

    #print(c1.deposit(-100))

    c2 = CheckingAccount("Charlie Lee", "2021-07-27", 500)
    #print(display_largest_account(Account.list_accounts))

    #print(display_oldest_account(Account.list_accounts))





if __name__ == '__main__':
    main()