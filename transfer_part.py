import datetime
from datetime import date
import json
import os
from loading_saving_data import load_data,save_data


def transfer_part(database,user_account):
    users_list = database["users"]

    #-------------------------------------
    print("Sender: ",user_account)
    recipient_number=input("Recipient: ")
    
    #------------------------
    rec_info = next(
        (
            user for user in users_list if user.get("account_number") == recipient_number),None)
    #------------------------
    if rec_info:
        recipient_account=rec_info.get("username")
        print("Recipient account: ",recipient_account)
        amount=int(input("Amount (AZN): "))
        amount*=100
        confirm=input("Confirm transfer (Y/N): ")
        today_str=date.today().strftime("%Y-%m-%d")
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
            print("")
            print("Transfer successful.")
            user_info["balance"]-=amount
            rec_info["balance"]+=amount
            user_info["last_transfer_date"]=today_str
            user_info["daily_transfer_count"]+=1
            print("Sender new balance: ",user_info["balance"]/100)
            history_line="Date: "+str(datetime.datetime.now())+"/"+"Type: Trannsfer sent/"+"Recipient account:"+rec_info.get("account_number")+"/"+"Amount: -"+str(amount/100)+" AZN/"+"Balance before:"+str((user_info.get("balance")+amount)/100)+" AZN/"+"Balance after:"+str((user_info.get("balance")/100))+","
            user_info["history"]+=history_line
            history_line="Date: "+str(datetime.datetime.now())+"/"+"Type: Trannsfer recieved/"+"Sender account:"+user_info.get("account_number")+"/"+"Amount: "+str(amount)+" AZN/"+"Balance before:"+str((user_info.get("balance")-amount)/100)+" AZN/"+str((user_info.get("balance")/100))+","
            rec_info["history"]+=history_line
            save_data(database)
    else:
        print("Wrong account information")