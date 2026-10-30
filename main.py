import datetime
from datetime import date
import json
import os

FILENAME = "data.json"


def load_data():


  with open(FILENAME, "r") as file:
    return json.load(file)



def save_data(data):
  with open(FILENAME, "w") as file:
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
rec_info =next(
    (
        user for user in users_list if user.get("account_number") == recipient_number),None)
#------------------------
user_info =next(
    (user for user in users_list if user.get("username") == user_account), None)
if user_info.get("last_transfer_date")!=today_str:
    user_info["daily_transfer_count"]=0
    save_data(database)
if not(rec_info) or rec_info==user_info or rec_info.get("status")!="Active" or rec_info.get("username")!=recipient_account:
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
    print("")
    print("Transfer successful.")
    user_info["balance"]-=amount
    rec_info["balance"]+=amount
    user_info["daily_transfer_count"]+=1
    print("Sender new balance: ",user_info["balance"])
    history_line="Date: "+str(datetime.datetime.now())+"/"+"Type: Trannsfer sent/"+"Recipient account: "+rec_info.get("account_number")+"/"+"Amount: -"+str(amount)+" AZN/"+"Balance before:"+str(user_info.get("balance")+amount)+" AZN/"+"New balance: "+str(user_info.get("balance"))
    user_info["history"]+=history_line
    history_line="Date: "+str(datetime.datetime.now())+"/"+"Type: Trannsfer recieved/"+"Sender account: "+user_info.get("account_number")+"/"+"Amount: "+str(amount)+" AZN/"+"Balance before:"+str(user_info.get("balance")-amount)+" AZN/"+"New balance: "+str(user_info.get("balance"))
    rec_info["history"]+=history_line
    save_data(database)

"""Last_transfer_date-lər doldurulmalı, cari istifadəçiyə uyğun user_account doldurulmalıdır"""