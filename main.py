import Banking

if __name__=="__main__":

    b = Banking.Bank_Accounts()

    b.add_random_users(10, 3, 5)

    b.file_of_all_accounts()

    b.show_all()

