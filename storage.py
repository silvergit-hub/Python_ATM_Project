import json
def create_default_user_data(data_file):
    with open(data_file,"w",encoding="utf-8") as file:
        defaut_users = [{
            "user01" :{
                "username": "user001",
                "password": "Test@123",
                "account_number":"10010001",
                "balance": "2500.0",
                "attempts": 6,
                "isActive": True
            }},
            {
            "user02" :{
                "username": "user002",
                "password": "Test@456",
                "account_number":"10010002",
                "balance": "1500.0",
                "attempts": 6,
                "isActive": True
            }},
            {
            "user03" :{
                "username": "user003",
                "password": "Test@789",
                "account_number":"10010003",
                "balance": "3000.0",
                "attempts": 6,
                "isActive": True
            }}
        ]
        user_list = load_data(data_file)
        if user_list == []:
            json.dump(defaut_users,file,indent=4)

def load_data(data_file):
    user_list = []
    try:
        with open(data_file,"r",encoding="utf-8") as file:    
            user_list = json.load(file)
    except:
        user_list = []
    return user_list

def add_user(list,data_file,username,password,balance):
    with open(data_file,"w", newline="",encoding="utf-8") as file:
        user_data = {
            username:{
            "username": username,
            "password": password,
            "account_number": None,
            "balance": balance,
            "attemps": 6,
            "isActive": True
        }
        }
        list.append(user_data)
        # Send data to json
        json.dump(list,file,indent=4)
