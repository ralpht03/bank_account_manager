import tkinter as tk
from assignment3 import Account, SavingsAccount, CheckingAccount
from assignment3 import display_oldest_account, display_largest_account

app = tk.Tk()
app.title("Bank Account Manager")


# function to create a new savings account
def create_savings_account():
    name = name_entry.get()
    open_date = open_date_entry.get()
    balance = float(balance_entry.get())
    interest = float(interest_entry.get())

    savings_account = SavingsAccount(name, open_date, balance, interest)
    display_text.insert(tk.END, savings_account.display_info() + "\n")


# function to create a new checking account
def create_checking_account():
    name = name_entry.get()
    open_date = open_date_entry.get()
    balance = float(balance_entry.get())

    checking_account = CheckingAccount(name, open_date, balance)
    display_text.insert(tk.END, checking_account.display_info() + "\n")


# function to withdraw money from an account
def withdraw_money():
    amount = float(withdraw_entry.get())
    selected_account = Account.list_accounts[account_listbox.curselection()[0]]
    result = selected_account.withdraw(amount)
    display_text.insert(tk.END, result + "\n")


# function to deposit money into an account
def deposit_money():
    amount = float(deposit_entry.get())
    selected_account = Account.list_accounts[account_listbox.curselection()[0]]
    result = selected_account.deposit(amount)
    display_text.insert(tk.END, result + "\n")


# function to display information about the largest account
def display_largest():
    result = display_largest_account(Account.list_accounts)
    display_text.insert(tk.END, result + "\n")


# function to display information about the oldest account
def display_oldest():
    result = display_oldest_account(Account.list_accounts)
    display_text.insert(tk.END, result + "\n")


# creating gui components
name_label = tk.Label(app, text="Name:")
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

open_date_label = tk.Label(app, text="Open Date (YYYY-MM-DD):")
open_date_label.pack()

open_date_entry = tk.Entry(app)
open_date_entry.pack()

balance_label = tk.Label(app, text="Initial Balance:")
balance_label.pack()

balance_entry = tk.Entry(app)
balance_entry.pack()

interest_label = tk.Label(app, text="Interest Rate (for savings accounts only):")
interest_label.pack()

interest_entry = tk.Entry(app)
interest_entry.pack()

create_savings_button = tk.Button(app, text="Create Savings Account", command=create_savings_account)
create_savings_button.pack()

create_checking_button = tk.Button(app, text="Create Checking Account", command=create_checking_account)
create_checking_button.pack()

withdraw_label = tk.Label(app, text="Withdraw Amount:")
withdraw_label.pack()

withdraw_entry = tk.Entry(app)
withdraw_entry.pack()

withdraw_button = tk.Button(app, text="Withdraw", command=withdraw_money)
withdraw_button.pack()

deposit_label = tk.Label(app, text="Deposit Amount:")
deposit_label.pack()

deposit_entry = tk.Entry(app)
deposit_entry.pack()

deposit_button = tk.Button(app, text="Deposit", command=deposit_money)
deposit_button.pack()

account_listbox = tk.Listbox(app)
account_listbox.pack()

display_largest_button = tk.Button(app, text="Display Largest Account", command=display_largest)
display_largest_button.pack()

display_oldest_button = tk.Button(app, text="Display Oldest Account", command=display_oldest)
display_oldest_button.pack()

display_text = tk.Text(app)
display_text.pack()

app.mainloop()
