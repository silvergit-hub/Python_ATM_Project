import storage
import json

# file links valuable for easy access
user_data_file = "data/users.json"

with open(user_data_file,"r",encoding="utf-8")as file:
    try:
        user_list = json.load(file)
    except:
        user_list = []
    if user_list == []:
        storage.create_default_user_data()
        print("Default data loaded.")

# Simple inputs for test
# username = input("Enter Username: ")
# password = input("Enter Password: ")
# balance = input("Enter Balance: ")

# New user
# # user_list = []
# user_list = storage.load_data(user_data_file)
# storage.add_user(user_list,username,password,balance)

# Change password
# print("--Change password--")
# storage.change_password(input("Username: "),input("Newpassword: "))

# Withdrawal
# while True:
#     username = input("Enter Username: ")
#     if username == "exit":
#         break
#     amount = input("Enter withdrawal amount: ")
#     storage.change_balance(username,amount,"w")
    
# Deposit
while True:
    username = input("Enter Username: ")
    if username == "exit":
        break
    amount = input("Enter deposit amount: ")
    storage.change_balance(username,amount,"d")
    