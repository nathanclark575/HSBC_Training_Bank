import Banking

if __name__=="__main__":

    b = Banking.Bank_Accounts()

    b.add_user("nathan")
    b.add_user("dan")

    b.add_account("nathan")
    b.add_account("nathan")

    b.add_account("dan")

    b.make_transaction("nathan", 0, 1000, "CR")
    b.make_transaction("nathan", 1, 2000, "CR")
    b.make_transaction("dan", 0, 3000, "CR")

    print(b.bank_accounts)

    b.show_all()