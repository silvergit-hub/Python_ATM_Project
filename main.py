import json

import storage
import withdrawals
import depositsAndLimits
import atm

# file links valuable for easy access
user_data_file = "data/users.json"
atm_data_file = "data/atm.json"

# Create default user data if json file is empty
with open(user_data_file,"r",encoding="utf-8")as file:
    try:
        user_list = json.load(file)
    except:
        user_list = []
    if user_list == []:
        storage.create_default_user_data()
        print("Default data loaded.")

# Check for daily resets every time a user logs in
atm.check_daily_reset()

# Simple inputs for test
username = input("Enter Username: ")
# password = input("Enter Password: ")
# balance = input("Enter Balance: ")

# New user
# # user_list = []
# user_list = storage.load_data(user_data_file)
# storage.add_user(user_list,username,password)

# Change password
# print("--Change password--")
# storage.change_password(input("Username: "),input("Newpassword: "))

#withdrawals
# while True:
#     username = input("Enter Username: ")
#     if username == "exit":
#         break
#     amount = input("Enter withdrawal amount: ")
#     withdrawals.withdrawal(username,amount)

# Show Daily Limits
#depositsAndLimits.show_daily_limits(username)
