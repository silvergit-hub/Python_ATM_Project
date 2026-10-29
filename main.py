from datetime import date
import json
import os

FILENAME = "data.json"


def load_data():
  with open(FILENAME, "r", encoding="utf-8") as file:
    return json.load(file)


def save_data(data):
  with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
def find(lists,element):
    for elements in lists:
        if element==elements:
            return True
    return False
database = load_data()
users_list = database["users"]
user_reci_account=database["account_number"]
last_transfer_date=""
recipient_account_list=[]
amount_list=database["balance"]
user_status=database["status"]
hisory_list=[]
transfer_count=0
user_account="" #user_account hal-hazırda hesaba giriş edən istifadəçinin hesabıdır
user_amount=0   #user_amount hal-hazırda hesaba giriş edən istifadəçinin hesabındakı pul miqdarıdır
print("Sender: ",user_account)
recipient_account=input("Recipient account: ")
recipient=input("Recipient: ")
recipient=int(recipient)
amount=input("Amount (AZN): ")
amount=int(amount)
confirm=input("Confirm transfer (Y/N): ")
today_str=date.today().strftime("%Y-%m-%d")
if last_transfer_date!=today_str:
    transfer_count=0
if find(recipient_account_list,recipient_account)==False or user_reci_account==recipient_account:
    print("Wrong account informaation")
    print("Transfer unsuccesfully")
elif amount>user_amount or amount<=0:
    print("Insufficient amount of money")
    print("Transfer unsuccesfully")
elif transfer_count>=5:
    print("You reached daily limits")
    print("Transfer unsuccesfully")
elif confirm!="Y":
    print("Transfer rejected")
else:
    print("Transfer successful.")
    user_amount-=amount
    transfer_count+=1
    order=user_list.index(recipient)
    amount_list[order]+=amount
    print("Sender new balance: ",user_amount)
