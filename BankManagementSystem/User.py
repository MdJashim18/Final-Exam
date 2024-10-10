import random
from datetime import datetime
class Users:
    Account = {}
    flag = True
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = 0
        self.total_loan = 0
        self.account_num = self.auto_generate()
        self.transaction_history = []
        self.Account[self.account_num] = self

    def auto_generate(self):
        return random.randint(1,1000)

    def deposit(self,amount):
        self.balance+=amount
        self.transaction_history.append((datetime.now(),f"Deposte amount {amount}"))

    def withdraw_amount(self,amount):
        if self.is_bank_bankrupt()==False:
            if amount > self.balance:
                print(f"Withdrawal amount exceeded")
            else:
                self.balance -= amount
                self.transaction_history.append((datetime.now(), f"Withdrawal amount {amount}"))
        else:
            print("The bank is bankrupt")

    def check_available_balance(self):
        print(f"Balance : {self.balance}")
    
    def check_transaction_history(self):
        print("*****Transaction History*****")
        for trans in self.transaction_history:
            print(f"{trans[0]} - {trans[1]}")

    def take_loan(self,amount):
        if self.flag==True:
            if self.loan >= 2:
                print("Loan limit exceeded!")
            else:
                self.loan += 1
                self.total_loan+=amount
                self.balance += amount
                self.transaction_history.append((datetime.now(), f"Loan taken {amount}"))
        else:
            print(f"Loan feature off")

    def transfer(self,amount,acc_num):
        if self.is_bank_bankrupt()==False:
            if acc_num not in self.Account:
                print("Account does not exist")
            else:
                if amount > self.balance:
                    print("Transfer amount exceeds balance")
                else:
                    self.balance -= amount
                    self.Account[acc_num].balance += amount
                    self.transaction_history.append((datetime.now(), f"Transfer {amount} from {self.account_num} to {acc_num}"))
        else:
            print("The bank is bankrupt")
    

    def is_bank_bankrupt(self):
        total = sum([acc.balance for acc in self.Account.values()])
        if total==0:
            return True
        else:
            return False
        
