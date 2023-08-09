"""
    Bank_Accounts is for all of those in the bank
"""

import csv
import names
import random
import json
from tabulate import tabulate

class Bank_Accounts:


    # this initilizes the bank accounts for the whole bank
    def __init__(self):
        self.bank_accounts = {}
        self.number_of_statments = 0

    # run the system
    """
        1. add user
        2. add account
        3. print a statment for an account
        4. make transaction
        5. Show Ballance
        6. Set overdraft
        7. exit
        8. view accounts for a user
    """
    def caller(self):
        print("Hello, welcome to the Bank 1.0")
        print("What would you like to do?")
        print("1. add user")
        print("2. add account")
        print("3. print a statment for an account")
        print("4. Make a transaction")
        print("5. Get ballance")
        print("6. Set overdraft")
        print("7 Exit")
        print("8 view accounts for a user")
        print("9 print everything")
        print("10 add a random user")
        option = input()

        if option == "1":
            userID = input("userID = ")
            self.add_user(userID)

        if option == "2":
            userID = input("userID = ")
            self.add_account(userID)

        if option == "3":
            userID = input("userID = ")
            account_number = int(input("account number = "))
            self.statment_csv(userID, account_number)

        if option == "4":
            userID = input("userID = ")
            account_number = int(input("account number = "))
            amount = int(input("ammount = "))
            type = input("Type? DR/CR = ")

            self.make_transaction(userID, account_number, amount, type)

        if option == "5":
            userID = input("userID = ")
            account_number = int(input("account number = "))
            ballance = self.get_ballance(userID, account_number)

            print(f"ballance is {ballance}")

        if option == "6":
            userID = input("userID = ")
            account_number = int(input("account number = "))
            limit = int(input("Overdraft limit = "))

            self.set_overdraft(userID, account_number, limit)

        if option == "7":
            return

        if option == "8":
            userID = input("userID = ")
            number_of_accounts = self.get_number_of_accounts(userID)
            account_number = int(input(f"Your accounts are {[i for i in range(number_of_accounts)]} which account would you like to see? = "))

            print(self.get_account(userID, account_number))

        if option == "9":
            self.print_all()

        if option == "10":
            number_of_accounts = int(input("number of accounts = :"))
            number_of_transfers = int(input("number of transfers = :"))
            self.random_user(number_of_accounts, number_of_transfers)

        # continue?
        ans = input("Do you wish to continue? y/n = ")
        if ans == "y":
            self.caller()
        return


    # This allows for a user to be added
    def add_user(self, userID):


        # check to see if user already exits
        if userID in self.bank_accounts:
            print("User already exits")
            return

        user = {
            "userID" : userID,
            "accounts" : []
        }

        self.bank_accounts[userID] = user

    # This adds an account to the user
    def add_account(self, userID, ballance=0, overdraft=0):

        # check to see if userID exits
        if not userID in self.bank_accounts:
            print("User does not exits")
            return

        # gets the number of that account for the user
        account_number = len(self.bank_accounts[userID]["accounts"])

        account = {
            "account_number" : account_number,
            "ballance" : ballance,
            "overdraft" : overdraft,
            "transactions" : []
        }

        self.bank_accounts[userID]["accounts"].append(account)

    # add a transaction, go through and make this look nicer
    def make_transaction(self, userID, account_number, ammount, type):

        # get the account
        account = self.bank_accounts[userID]["accounts"][account_number]
        account_ballance = account["ballance"]

        # info to put in transaction statment
        transaction_succsess = "Allowed"
        # make this date later
        transaction_number = len(account["transactions"])

        # check to see if the account can occour, if it can't reccord it
        if type == "DR":
            if ammount > account_ballance:
                transaction_succsess = "Denied"
            # if not, update the ballance
            else:
                account_ballance -= ammount
                account["ballance"] = account_ballance
            transaction = [transaction_number, ammount, type,transaction_succsess]
            account["transactions"].append(transaction)

        if type == "CR":
            account_ballance += ammount
            account["ballance"] = account_ballance
            transaction = [transaction_number, ammount, type, transaction_succsess]
            account["transactions"].append(transaction)

    # function to return a csv statment for an account
    def statment_csv(self, userID, account_number):

        # get all the info that needs to be sent to the csv
        account = self.bank_accounts[userID]["accounts"][account_number]
        account_ballance = account["ballance"]
        transactions = account["transactions"]

        # statment name
        statment_name = f"/Users/nathanclark/Desktop/Statements/{self.number_of_statments}"


        account_info = [f"userID = {userID}", f"account number = {account_number}", f"ballance = {account_ballance}", f"overdraft = {account['overdraft']}"]
        header = ["transaction number", "ammount", "type", "allowed"]

        # make csv
        with open(statment_name, "w") as file:

            writer = csv.writer(file)

            writer.writerow(account_info)
            writer.writerow(header)
            writer.writerows(transactions)

        self.number_of_statments += 1

    # get ballance
    def get_ballance(self, userID, account_number):
        account = self.bank_accounts[userID]["accounts"][account_number]
        ballance = account["ballance"]
        return ballance

    # set overdraft
    def set_overdraft(self, userID, account_number, limit):
        account = self.bank_accounts[userID]["accounts"][account_number]
        account["overdraft"] = limit
        return

    # get number of accounts
    def get_number_of_accounts(self, userID):
        return len(self.bank_accounts[userID]["accounts"])

    # return account
    def get_account(self, userID, account_number):
        return self.bank_accounts[userID]["accounts"][account_number]

    # make a random user with a number of accounts
    def random_user(self, number_number_of_accounts=1, number_of_transactions=1):

        # make user
        userID = names.get_full_name()
        self.add_user(userID)

        # make a number of accounts
        for account_number in range(number_number_of_accounts):

            # get random ballance and overdraft
            ballance = round(random.randint(0, 5000), 2)
            overdraft = 0

            # 1 in 10 change on an overdraft
            rand = random.randint(0, 9)
            if rand == 5:
                overdraft = ballance * 0.1

            self.add_account(userID, round(ballance, 2), overdraft)

            # then add transactions to that account
            for transaction in range(number_of_transactions):

                amount = round(random.randint(0, 13) / 10 * ballance, 2)
                type = "CR"

                # make chace of CR to DR 1:1
                chance = random.randint(0, 1)
                if chance == 1:
                    type = "DR"

                self.make_transaction(userID, account_number, round(amount, 2), type)


    # show all stuff for system
    def print_all(self):
        print(self.bank_accounts)

    # add multiple random users
    def add_random_users(self, number_of_users, number_of_accounts, number_of_transactions):
        for i in range(number_of_users):
            self.random_user(number_of_accounts, number_of_transactions)

    # add all to a csv
    def file_of_all_accounts(self):

        file = "/Users/nathanclark/Desktop/all/all_data"
        data = json.dumps(self.bank_accounts)

        with open(file, "w") as f:
            f.write(data)

    # show one account in a nice form
    def show_account(self, userID, account_number):

        # get the account
        account = self.bank_accounts[userID]["accounts"][account_number]
        ballance = self.get_ballance(userID, account_number)

        # make the header
        header = ["transaction number", "amount", "type", "sucsess?"]
        account_transactions = account["transactions"]

        print("----------------")
        print(f"The ballance for account {account_number} is {ballance}")
        print(tabulate(account_transactions, header))


    # show user
    def show_user(self, userID):

        user_info = self.bank_accounts[userID]
        accounts = user_info["accounts"]


        print("---------------")
        print(f"userID = {userID}")

        for i in range(len(accounts)):
            self.show_account(userID, i)


    # show all accounts
    def show_all(self):
        for key in self.bank_accounts.keys():
            self.show_user(key)
