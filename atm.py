import time
print('\033[1;32;40m Bright Green \n')
print('\n\n\t\t\t\t\t\t Welcome to the SBI Bank ATM')
print("\n\n\n\t\t please insert your card")
time.sleep(5)
password = 1234
pin = int(input('\n\n\t\t enter your pin:'))
balance = 5000
while True:
    if pin == password:
        print("""
        1.balance\n
        2.withdraw balance\n
        3.deposit balance\n
        4.exit""")
        try:
            option = int(input("\n enter your option"))
        except:
            print("\n enter valid option")
        if option == 1:
            print(f"\n your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("\n please enter your withdraw amount:"))
            balance = balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"\n your updated balance is {balance}")
        elif option == 3:
            deposit_amount = int(input("\n enter the amount you want to deposit:"))
            print(f" your credited amount is {deposit_amount} ") 
            balance = deposit_amount+balance
            print(f" your current balance is {balance}")
        elif option == 4:
            break
        else:
            print('\n Sorry! you choosed wrong option\n Please try again')