import time

default_users = [
            {
                "username": "user001",
                "password": "Test@123",
                "account_number":"10010001",
                "balance": "2500.0",
                "status": "Blocked",
                "attempts": 6,
                "daily_withdrawal_amount":"0.0",
                "daily_deposit_amount": "0.0",
                "daily_transfer_count":0,
                "last_transaction_date":""
            },
            {
                "username": "user002",
                "password": "Test@456",
                "account_number":"10010002",
                "balance": "1500.0",
                "status": "Active",
                "attempts": 6,
                "daily_withdrawal_amount":"0.0",
                "daily_deposit_amount": "0.0",
                "daily_transfer_count":0,
                "last_transaction_date":""            
            },
            {
                "username": "user003",
                "password": "Test@789",
                "account_number":"10010003",
                "balance": "3000.0",
                "status": "Active",
                "attempts": 6,
                "daily_withdrawal_amount":"0.0",
                "daily_deposit_amount": "0.0",
                "daily_transfer_count":0,
                "last_transaction_date":""
            }
        ]
def authentication():
    while True:
        user_found=False
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        for i in range(0, len(default_users)):
            if default_users[i]["username"]==username:
                user_found=True
                if default_users[i]["status"]=="Blocked":
                    print("Your account is blocked!")
                elif default_users[i]["password"]==password:
                    print("Welcome,",username)
                    break
                elif default_users[i]["attempts"] <= 3:
                    default_users[i]["status"] = "Temporarily Blocked"
                    print("Your account is temporarily blocked!")
                    for i in range (60,0,-1):
                        print("Please wait for",i,"seconds to try again.")
                        time.sleep(1)
                elif default_users[i]["attempts"] == 0:
                    default_users[i]["status"] = "Blocked"
                    print("Your account is permanently blocked!")
                else:
                    print("Wrong password!")
                    default_users[i]["attempts"]-=1
                    print("Left attempts:",default_users[i]["attempts"])

              
            if user_found==False:
                print("Username or password is wrong!")
authentication()
def change_password():
    username=input("Enter your username: ")
    password=input("Enter your current password: ")
    for i in range(0, len(default_users)):
        if default_users[i]["username"]==username:
            if default_users[i]["password"]==password:
                new_password=input("Enter your new password: ")
                #storage.change_password(username, new_password)


