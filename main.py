import json

import storage
import atm
import auth

# file links valuable for easy access
user_data_file = "data/users.json"
atm_data_file = "data/atm.json"

def check_json_files(file_path,type):
    try:
        with open(file_path,"r",encoding="utf-8")as file:
            data_list = json.load(file)
    except:
        data_list = []
    if data_list == [] and type =="user" :
        storage.create_default_user_data()
    elif data_list == [] and type == "atm":
        storage.create_default_atm_data()

# Check for daily resets every time a user logs in
atm.check_daily_reset()

# Create default data files if json file is empty or not exist
check_json_files(user_data_file,"users")
check_json_files(atm_data_file,"atm")

# Start the authentication process
auth.authentication()