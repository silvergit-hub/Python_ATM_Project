import json
user_data_file = "data/users.json"
from decimal import Decimal

def load_data():
    user_list = []
    try:
        with open(user_data_file,"r",encoding="utf-8") as file:    
            user_list = json.load(file)
            print("Data loaded.")
    except:
        user_list =[]
        print("File not found.")
    return user_list

def save_data(user_list):
    with open(user_data_file,"w",encoding="utf-8") as file:
        json.dump(user_list,file,indent=4)
        print("Data sended.")

def create_default_user_data():
    with open(user_data_file,"w",encoding="utf-8") as file:
        defaut_users = [
            {
                "username": "user001",
                "password": "Test@123",
                "account_number":"10010001",
                "balance": "2500.0",
                "attempts": 6,
                "isActive": True
            },
            {
                "username": "user002",
                "password": "Test@456",
                "account_number":"10010002",
                "balance": "1500.0",
                "attempts": 6,
                "isActive": True
            },
            {
                "username": "user003",
                "password": "Test@789",
                "account_number":"10010003",
                "balance": "3000.0",
                "attempts": 6,
                "isActive": True
            }
        ]
        json.dump(defaut_users,file,indent=4)
        print("Yes")

def add_user(user_list,username,password):
    with open(user_data_file,"w", newline="",encoding="utf-8") as file:
        account_number =user_list[-1]
        account_number = str(int(account_number["account_number"])+1)
        user_data = {
            "username": username,
            "password": password,
            "account_number": account_number,
            "balance": "0",
            "attemps": 6,
            "isActive": True
        }
        user_list.append(user_data)
        # Send data to json
        json.dump(user_list,file,indent=4)
        print("User added.")

def change_password(username,new_password):
    user_data = load_data()
    user_found = False
    for i in range(0,len(user_data)):
        if user_data[i]["username"] == username:
            user_data[i]["password"] = new_password
            user_found = True
            print(user_data)
    if user_found == False:
        print("User not found.")
    save_data(user_data)

def change_balance(username,amount,action):
    user_data = load_data()
    # Withdraw
    if action == "w":
        for i in range(0,len(user_data)):
            if user_data[i]["username"] == username:
                balance = Decimal(user_data[i]["balance"])
                amount = Decimal(amount)
                if balance >= amount:
                    balance -=amount
                    user_data[i]["balance"] = str(balance)
                    print("Withdrawaled Cash:",amount)
                    print("Current Balance:",balance)
                else:
                    print("Invalid Amount.")
    #Deposit
    elif action == "d":
        for i in range(0,len(user_data)):
            if user_data[i]["username"] == username:
                balance = Decimal(user_data[i]["balance"])
                amount = Decimal(amount)
                balance += amount
                user_data[i]["balance"] = str(balance)
                print("Deposited Cash:",amount)
                print("Current Balance:",balance)
    save_data(user_data)