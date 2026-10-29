from datetime import date
import json
import os

FILENAME = "data.json"


def load_data():
  if not os.path.exists(FILENAME):
    default_data = {
        "users": [
            {
                "username": "user01",
                "password": "Test@123",
                "account_number": "10010001",
                "balance": 2500.0,
                "status": "Active",
                "daily_transfer_count": 0,
                "last_transfer_date": "",
            },
            {
                "username": "user02",
                "password": "Test@456",
                "account_number": "10010002",
                "balance": 1500.0,
                "status": "Active",
                "daily_transfer_count": 0,
                "last_transfer_date": "",
            },
            {
                "username": "user03",
                "password": "Test@789",
                "account_number": "10010003",
                "balance": 3000.0,
                "status": "Active",
                "daily_transfer_count": 0,
                "last_transfer_date": "",
            },
        ]
    }
    save_data(default_data)
    return default_data

  with open(FILENAME, "r", encoding="utf-8") as file:
    return json.load(file)



def save_data(data):
  with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

database = load_data()
users_list = database["users"]

#-------------------------------------
user_account="user01" #user_account hal-hazırda hesaba giriş edən istifadəçinin hesabıdır
#--------------------------------------
print("Sender: ",user_account)
recipient_account=input("Recipient account: ")
recipient_number=input("Recipient: ")
amount=input("Amount (AZN): ")
amount=int(amount)
confirm=input("Confirm transfer (Y/N): ")
today_str=date.today().strftime("%Y-%m-%d")
#------------------------
rec_info = next(
    (
        user for user in users_list if user.get("account_number") == recipient_number),None,)
#------------------------
user_info = next(
    (user for user in users_list if user.get("username") == user_account), None)
if user_info.get("last_transfer_date")!=today_str:
    user_info["daily_transfer_count"]=0
    save_data(database)
if not(rec_info) or rec_info==user_info or rec_info.get("status")!="Active":
    print("Wrong account informaation")
    print("Transfer unsuccesfully")
elif amount>user_info.get("balance") or amount<=0:
    print("Insufficient amount of money")
    print("Transfer unsuccesfully")
elif user_info.get("daily_transfer_count")>=5:
    print("You reached daily limits")
    print("Transfer unsuccesfully")
elif confirm!="Y":
    print("Transfer rejected")
else:
    print("Transfer successful.")
    user_info["balance"]-=amount
    rec_info["balance"]+=amount
    save_data(database)
    print("Sender new balance: ",user_info["balance"])

"""Last_transfer_date-lər doldurulmalı, cari istifadəçiyə uyğun user_account doldurulmalıdır"""