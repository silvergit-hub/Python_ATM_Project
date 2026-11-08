import storage
from decimal import Decimal

user_data_file = "data/users.json"
atm_data_file = "data/atm.json"

# ATM infos
atm_data_list = storage.load_data(atm_data_file)
storage.save_data(atm_data_file,atm_data_list)

# Daily limits
daily_deposit_limit = Decimal(atm_data_list["daily_deposit_limit"])
daily_withdrawal_limit = Decimal(atm_data_list["daily_withdrawal_limit"])
commission_free_withdrawal_limit = Decimal(atm_data_list["commision_free_withdrawal"])
daily_tranfer_limit = Decimal(atm_data_list["daily_transfer_limit"])

# Deposit function, but dont check amount value so you must check if amount is a float converted to str 
# because it is needed to use them with decimal function
def Depossit(username,amount):
    user_data = storage.load_data(user_data_file)
    atm_data = storage.load_data(atm_data_file)
    user_found = False

    amount = Decimal(amount)
    daily_atm_cash = Decimal(atm_data["daily_atm_cash"])
    for i in range(0,len(user_data)):
            if user_data[i]["username"] == username:
                user_found = True
                
                balance = Decimal(user_data[i]["balance"])
                daily_deposit_amount = Decimal(user_data[i]["daily_deposit_amount"])

                if amount>daily_deposit_limit:
                    print("=========================================================================")
                    print("Cash deposit earlier today:",daily_deposit_amount,"AZN")
                    print("Daily deposit Limit:",daily_deposit_limit,"AZN")
                    print("Remaining deposit amount:",daily_deposit_limit-daily_deposit_amount,"AZN")
                    print("You cannot deposit more than remaining amount.")
                    print("=========================================================================")
                    break
                balance += amount
                user_data[i]["balance"] = str(balance)
                user_data[i]["daily_deposit_amount"] = str(daily_deposit_amount+amount)
                atm_data["daily_atm_cash"] = str(daily_atm_cash + amount)
                
                print("=========================================================================")
                print("Cash deposit earlier today:",daily_deposit_amount,"AZN")
                print("Daily deposit Limit:",daily_deposit_limit,"AZN")
                print("Remaining deposit amount:",daily_deposit_limit-daily_deposit_amount-amount,"AZN")
                print("Deposited Cash:",amount,"AZN")
                print("Current Balance:",balance,"AZN")
                print("=========================================================================")

    if user_found == False:
        print("User not found.")
    storage.save_data(user_data_file,user_data)
    storage.save_data(atm_data_file,atm_data)

# Show all the daily limits of the user in one screen
def show_daily_limits(username):
    user_data = storage.load_data(user_data_file)
    
    for i in range(0,len(user_data)):
        if user_data[i]["username"] == username:
            daily_deposit_amount = Decimal(user_data[i]["daily_deposit_amount"])
            daily_withdrawal_amount = Decimal(user_data[i]["daily_withdrawal_amount"])
            daily_transfer_count = Decimal(user_data[i]["daily_transfer_count"])
            daily_commission_free_withdrawal_amount = commission_free_withdrawal_limit - daily_withdrawal_amount
            if daily_commission_free_withdrawal_amount < 0:
                daily_commission_free_withdrawal_amount = 0

    print("==================== DAILY LIMITS ====================")
    print(f"Deposit used:             {daily_deposit_amount} / {daily_withdrawal_limit} AZN")
    print(f"Deposit remainig:         {daily_withdrawal_limit-daily_deposit_amount} AZN")    
    print(f"Cash withdrawn:           {daily_withdrawal_amount} / {daily_withdrawal_limit} AZN")
    print(f"Cash withdrawal reamining:{daily_withdrawal_limit-daily_withdrawal_amount} AZN")
    print(f"Fee-free cash remaining:  {daily_commission_free_withdrawal_amount} AZN")
    print(f"Outgoing transfers:       {daily_transfer_count} / {daily_tranfer_limit}")
    print("=====================================================")

    storage.save_data(user_data_file,user_data)