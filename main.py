import json

import storage
import atm
import auth
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

# Start the authentication process
auth.authentication()