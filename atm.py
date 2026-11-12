import storage

from datetime import date

user_data_file = "data/users.json"
atm_data_file = "data/atm.json"

default_daily_atm_cash = "5000.0"

atm_data = storage.load_data(atm_data_file)
user_data = storage.load_data(user_data_file)

#We must send them because if we didnt the json files will be empty
storage.save_data(atm_data_file,atm_data)
storage.save_data(user_data_file,user_data)

# I will check it every time person logs in system but because of notexisting auth.py 
# i will just simulate little version of login
def check_daily_reset():
    today_date = date.today()
    if str(today_date) != atm_data["last_reset_date"]:
        atm_data["last_reset_date"] = str(today_date)
        atm_data["daily_atm_cash"] = default_daily_atm_cash
        for i in range(0,len(user_data)):
            user_data[i]["daily_withdrawal_amount"] = "0.0"
            user_data[i]["daily_deposit_amount"] = "0.0"
            user_data[i]["daily_transfer_count"] = 0
        storage.save_data(user_data_file,user_data)
        storage.save_data(atm_data_file,atm_data)
