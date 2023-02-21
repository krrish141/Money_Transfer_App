class Gpay:
    print("Welcome To Gpay")

    def Moneytransfer(self):
        balance = 10000
        numbers = int(input('''
            1  8070244909
            2  9845621312
            3  5648945645
            4  5647992131
            5  9456321455
            6  9845621312
            8  5648945565
            9  5647992131
            10 9455632145
            '''))

        if numbers == 1 or numbers == 2 or numbers == 3 or numbers == 4 or numbers == 5 or numbers == 6 or numbers == 7 or numbers == 8 or numbers == 9 or numbers == 10:
            print("Confirm This Number you want send Money")

        else:
            print("Enter the Valid Number")

        amount = int(input("Enter amount : "))
        if amount > 0 and amount <= balance:
            new_bal = balance - amount
            print("Amount", amount, "successfully debited from your account and new balance is ",new_bal)
        else:
            print("Not enough cash in your account ")

    def reacharge(self):
        balance = 10000
        recharge = int(input("Enter the Recharge Number : "))
        # if recharge > 0 and recharge <= :
        #     print("done")
        # else:
        #     print("Enter 10 ")
        #     sys.exit()
        amount = int(input("Enter amount : "))
        if amount > 0 and amount <= balance:
            new_bal = balance - amount
            print("successfully Done", amount, "paid to ", recharge)
        else:
            print("Not enough money in your account ")

    def checkBalance(self):
        print("Hint = 123456")
        balance = 10000

        checkBalance = int(input("Enter The Pin : "))
        if checkBalance == 123456:
            print('you have Rs', balance, 'In Your Bank Account')
        else:
            print("Enter the 6 Digit Correct Pin")


while True:
    app = Gpay()

    User_Choice = int(input('''
    1 Moneytransfer
    2 Recharge
    3 CheckBalance
    4 Exit
    '''))
    if User_Choice == 1:
        app.Moneytransfer()

    elif User_Choice == 2:
        app.reacharge()

    elif User_Choice == 3:
        app.checkBalance()
    else:
        break