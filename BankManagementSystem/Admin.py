from User import Users
class Admin:
    def create_account(self,name,email,address,account_type):
        user = Users(name,email,address,account_type)
        Users.Account[user.account_num] = user
        return user
    
    def delete_account(self,acc_num):
        if acc_num in Users.Account:
            del Users.Account[acc_num]
        else:
            print(f"Account not found")
    
    def see_all_account(self):
        if len(Users.Account)==0:
            print(f"No one account")
        else:
            for user in Users.Account.values():
                print(f"{user.name},{user.email},{user.address},{user.account_type}")
    
    def check_total_balance(self):
        total = sum([acc.balance for acc in Users.Account.values()])
        print(f"Total balance : {total}")
    
    def total_loan(self):
        total_loan = sum([acc.total_loan for acc in Users.Account.values()])
        print(f"Total loan : {total_loan}")
    
    def loan_feature(self):
        if Users.flag:
            print(f"Current loan feature : {Users.flag}")
            Users.flag = False
        else:
            print(f"Current loan feature : {Users.flag}")
            Users.flag = True
