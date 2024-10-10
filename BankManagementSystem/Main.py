from User import Users
from Admin import Admin


def Users_menu(customer):
    while True:
        print("1: Deposit ")
        print("2: Withdraw ")
        print("3: check balance ")
        print("4: take loan ")
        print("5: Transfer amount ")
        print("6: Exit")

        ch = int(input("Enter your choice : "))
        if ch==1:
            amount = int(input("Enter amount : "))
            customer.deposit(amount)
        elif ch==2:
            amount = int(input("Enter amount : "))
            customer.withdraw_amount(amount)
        elif ch==3:
            customer.check_available_balance()
        elif ch==4:
            amount = int(input("Enter amount : "))
            customer.take_loan(amount)
        elif ch==5:
            amount = int(input("Enter amount : "))
            customer.transfer(amount,customer.auto_generate())
        elif ch==6:
            break
        else:
            continue



def admin_menu(admin):
    while True:
        print("1: create account ")
        print("2: delete account ")
        print("3: see all user accounts list ")
        print("4: check the total available balance ")
        print("5: check the total loan amount ")
        print("6: on or off the loan feature of the bank ")
        print("7: Exit")

        ch = int(input("Enter your choice : "))
        if ch==1:
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            address = input("Enter your address : ")
            account_type = input("Enter your account type : ")
            admin.create_account(name,email,address,account_type)
        elif ch==2:
            id = int(input("Enter your ID : "))
            admin.delete_account(id)
        elif ch==3:
            admin.see_all_account()
        elif ch==4:
            admin.check_total_balance()
        elif ch==5:
            admin.total_loan()
        elif ch==6:
            admin.loan_feature()
        elif ch==7:
            break
        else:
            continue



while True:
    print("*****WELCOME OUR TO BANK*****")
    print("1: For Users ")
    print("2: For Admin ")
    print("3: Exit")

    ch = int(input("Enter your choice : "))
    if ch==1:
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        address = input("Enter your address : ")
        account_type = input("Enter your account type : ")
        customer = Users(name,email,address,account_type)
        Users_menu(customer)
    elif ch==2:
        admin = Admin()
        admin_menu(admin)
    elif ch==3:
        break
    else:
        continue
