import datetime
import storage
from decimal import Decimal 

user_data_file = "data/users.json"

def transfer_part(database,user_account):
    users_list = database

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
        amount=input("Amount (AZN): ")
        confirm=input("Confirm transfer (Y/N): ")
        #------------------------
        user_info = next(
            (user for user in users_list if user.get("username") == user_account), None)
        
        if not(rec_info) or rec_info==user_info or rec_info.get("status")!="Active":
            print("Wrong account informaation")
            print("Transfer unsuccesfully")
        try:
            amount = Decimal(amount)
        except:
            print("Invalid amount")
            return
        if amount > Decimal(user_info.get("balance")) or amount<=0:
            print("Insufficient amount of money")
            print("Transfer unsuccesfully")
        elif round(amount,2) != amount:
            print("Amount must have at most 2 decimal places")
        elif user_info.get("daily_transfer_count")>=5:
            print("You reached daily limits")
            print("Transfer unsuccesfully")
        elif confirm!="Y":
            print("Transfer rejected")
        else:
            print("")
            print("Transfer successful.")

            user_balance = Decimal(user_info["balance"])
            rec_balance = Decimal(rec_info["balance"])

            user_new_balance = user_balance - amount
            rec_new_balance = rec_balance + amount

            # User data changes
            for i in range(0,len(users_list)):
                if users_list[i]["username"] == user_info["username"]:
                    
                    users_list[i]["balance"] = str(user_new_balance)
                    users_list[i]["daily_transfer_count"]+=1
                    
                    history_line="Date: "+str(datetime.datetime.now())+"/"+"Type: Trannsfer sent/"+"Recipient account:"+rec_info.get("account_number")+"/"+"Amount: -"+str(amount)+" AZN/"+"Balance before:"+str(user_balance)+" AZN/"+"Balance after:"+str(user_new_balance)+","
                    user_info["transaction_dates"]+=history_line
            print("Sender new balance: ", user_new_balance)

            # Recipient data changes
            for i in range(0,len(users_list)):
                if users_list[i]["username"] == rec_info["username"]:
                    users_list[i]["balance"] = str(rec_new_balance)
                    history_line="Date: "+str(datetime.datetime.now())+"/"+"Type: Trannsfer recieved/"+"Sender account:"+user_info.get("account_number")+"/"+"Amount: "+str(amount)+" AZN/"+"Balance before:"+str(rec_balance)+" AZN/"+"Balance after:"+str(rec_new_balance)+","
                    rec_info["transaction_dates"]+=history_line

            storage.save_data(user_data_file,users_list)
    else:
        print("Wrong account information")