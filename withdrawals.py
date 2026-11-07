import storage
from decimal import Decimal

user_data_file = "data/users.json"
atm_data_file = "data/atm.json"

# ATM infos
atm_data_list = storage.load_data(atm_data_file)
storage.save_data(atm_data_file,atm_data_list)

daily_withdrawal_limit = Decimal(atm_data_list["daily_withdrawal_limit"])
commision_free_withdrawal = Decimal(atm_data_list["commision_free_withdrawal"])
commision_fee = Decimal(atm_data_list["commision_fee"])

# Withdraw or Deposit but dont check amount value so you must check if amount is a float 
# converted to str because it is needed to use them with decimal function
def withdrawal(username,amount):
    user_data = storage.load_data(user_data_file)
    atm_data = storage.load_data(atm_data_file)
    user_found = False

    amount = Decimal(amount)
    daily_atm_cash = Decimal(atm_data["daily_atm_cash"])
    # Withdraw
    for i in range(0,len(user_data)):
        if user_data[i]["username"] == username:
            user_found = True
            
            balance = Decimal(user_data[i]["balance"])
            daily_withdrawal_amount = Decimal(user_data[i]["daily_withdrawal_amount"])
                
            if balance >= amount and daily_withdrawal_amount + amount <= daily_withdrawal_limit and daily_withdrawal_amount + amount<= commision_free_withdrawal and amount<=daily_atm_cash:
                balance -=amount
                user_data[i]["balance"] = str(balance)
                user_data[i]["daily_withdrawal_amount"] = str(daily_withdrawal_amount+ amount)
                atm_data_list["daily_atm_cash"] = str(daily_atm_cash - amount)
                print("=========================================================================")
                print("Cash withdrawn earlier today: ",daily_withdrawal_amount,"AZN")
                print("Withdrawaled Cash:",amount,"AZN")
                print("Current Balance:",balance,"AZN")
                print("=========================================================================")
            elif balance >= amount and daily_withdrawal_amount + amount <= daily_withdrawal_limit and daily_withdrawal_amount + amount >commision_free_withdrawal and amount<=daily_atm_cash:
                commision_free_withdrawal_amount = Decimal(commision_free_withdrawal - daily_withdrawal_amount)
                if commision_free_withdrawal_amount<0:
                    commision_free_withdrawal_amount = 0
                amount_applying_commision_on = Decimal(amount - commision_free_withdrawal_amount)
                commission = Decimal(amount_applying_commision_on * commision_fee)
                taken_cash = commision_free_withdrawal_amount + amount_applying_commision_on + commission
                balance = balance - taken_cash

                user_data[i]["balance"] = str(balance)                   
                user_data[i]["daily_withdrawal_amount"] = str(daily_withdrawal_amount + amount)
                atm_data["daily_atm_cash"] = str(daily_atm_cash - amount)

                print("=========================================================================")
                print("Cash withdrawn earlier today:",daily_withdrawal_amount,"AZN")
                print("Remaining fee-free allowance:",commision_free_withdrawal_amount,"AZN")
                print("Amount charged with commission:",amount_applying_commision_on,"AZN")
                print("Withdrawal Commision",commision_fee*100,"%:",commission,"AZN")
                print("Withdrawaled Cash:",amount,"AZN")
                print("Cash taken from account:",taken_cash,"AZN")
                print("Current Balance:",balance,"AZN")
                print("=========================================================================")
            elif daily_withdrawal_amount+amount>daily_withdrawal_limit:
                print("=========================================================================")
                print("Cash withdrawn earlier today:",daily_withdrawal_amount,"AZN")
                print("Daily withdrawal Limit:",daily_withdrawal_limit,"AZN")
                print("Remaining withdrawal amount:",daily_withdrawal_limit-daily_withdrawal_amount,"AZN")
                print("You cannot withdrawal more than remaining amount.")
                print("=========================================================================")
            elif daily_atm_cash < amount:
                print("Remaining cash in ATM:",daily_atm_cash,"AZN")
                print("You cannot withdrawal more than remaining cash today.")
            else:
                print("Cannot Withdrawal.")
    
    if user_found == False:
        print("User not found.")
    storage.save_data(user_data_file,user_data)
    storage.save_data(atm_data_file,atm_data)

