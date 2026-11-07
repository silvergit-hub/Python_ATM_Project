import json
user_data_file = "data/users.json"
atm_data_file = "data/atm.json"


def load_data(data_file):
    data_list = []
    try:
        with open(data_file,"r",encoding="utf-8") as file:    
            data_list = json.load(file)
            #print("Data loaded.")
    except:
        data_list =[]
        #print("File not found.")
    return data_list

def save_data(data_file,user_list):
    with open(data_file,"w",encoding="utf-8") as file:
        json.dump(user_list,file,indent=4)
        #print("Data sended.")

def create_default_user_data():
    with open(user_data_file,"w",encoding="utf-8") as file:
        defaut_users = [
            {
                "username": "user001",
                "password": "Test@123",
                "account_number":"10010001",
                "balance": "2500.0",
                "status": "Active",
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
        json.dump(defaut_users,file,indent=4)

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
    user_data = load_data(user_data_file)
    user_found = False
    for i in range(0,len(user_data)):
        if user_data[i]["username"] == username:
            user_data[i]["password"] = new_password
            user_found = True
            print(user_data)
    if user_found == False:
        print("User not found.")
    save_data(user_data_file,user_data)
