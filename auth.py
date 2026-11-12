import time

import storage
import withdrawals
import depositsAndLimits
from transaction import transaction_history_service
from datas_history import load_database,save_database


# file links valuable for easy access
user_data_file = "data/users.json"
atm_data_file = "data/atm.json"

# Load user and ATM data from JSON files
user_data = storage.load_data(user_data_file)
atm_data = storage.load_data(atm_data_file)

def login():
  while True:
    user_found=False
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    index = 0
    for i in range(0, len(user_data)):
      if user_data[i]["username"]==username:
        user_data[i]["attempts"] -=1
        user_found=True
        index = i
        if user_data[i]["status"]=="Blocked":
          print("Your account is blocked!")
        elif user_data[i]["password"]==password:
          print("Welcome,",username)
          user_data[i]["attempts"] = 6
        elif user_data[i]["attempts"] == 3:
          user_data[i]["status"] = "Temporarily Blocked"
          print("Your account got temporarily blocked!")
          for j in range (60,0,-1):
            print("Please wait for",j,"seconds to try again.")
            time.sleep(.1)
          user_data[i]["status"] = "Active"
        elif user_data[i]["attempts"] == 0:
          user_data[i]["status"] = "Blocked"
          print("Your account got permanently blocked!")
        else:
          print("Wrong password!")
          print("Left attempts:",user_data[i]["attempts"])  
        storage.save_data(user_data_file,user_data)      
    if user_found==False:
      print("Username or password is wrong")
    elif user_found and user_data[index]["status"] =="Active" and user_data[index]["password"]==password:
      break
    elif user_data[i]["attempts"] == 0 or user_data[i]["status"]=="Blocked":
      break
  main_menu(username) if user_found else authentication()

def signup():
  username=input("Enter your username: ")
  password=input("Enter your password: ")
  if storage.check_user_exists(username):
    print("This username is already taken. Please choose a different name.")
  elif len(password) < 8:
    print("Password must be at least 8 characters!")
  elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit!")
  elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter!")
  elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter!")
  else:
    storage.add_user(user_data,username,password)
    print("Signup successful!")
    main_menu(username)

def authentication():
  while True:
    print("""
======== Python Bank System ========
Welcome to the Python Banking System!
1.Log in
2.Sign up
3.Exit
====================================
    """)
    option=input("Select an option: ")
    match option:
      case "1":
        login()
        break
      case "2":
        signup()
        break
      case "3":
        print("Goodbye!")
        break
      case _:
        print("Invalid option!")

def change_password(username):
  print("============ Change Password =============")
  password=input("Enter your current password: ")
  for i in range(0, len(user_data)):
    if user_data[i]["username"]==username:
      if user_data[i]["password"]==password:
        new_password=input("Enter your new password: ")
        if len(new_password) < 8:
          print("Password must be at least 8 characters!")
        elif not any(char.isdigit() for char in new_password):
          print("Password must contain at least one digit!")
        elif not any(char.isupper() for char in new_password):
          print("Password must contain at least one uppercase letter!")
        elif not any(char.islower() for char in new_password):
          print("Password must contain at least one lowercase letter!")
        confirm_password=input("Confirm your new password: ")
        if new_password == confirm_password:
          storage.change_password(username,new_password)
          print("Password changed succesfully!")
        else:
          print("Passwords do not match!")

def show_account_info(username):
  for i in range(0,len(user_data)):
    if user_data[i]["username"] ==username:
      print("=========== Account Information ===========")
      print("Account Holder :",user_data[i]["username"])
      print("Account Number :",user_data[i]["account_number"])
      print("Available Balance :",user_data[i]["balance"])
      print("Account Status :",user_data[i]["status"])
      print("===========================================")

def show_account_balance(username):
  for i in range(0,len(user_data)):
    if user_data[i]["username"] ==username:
      print("=========== Account Information ===========")
      print("Account Holder :",user_data[i]["username"])
      print("Current Balance :",user_data[i]["balance"])
      print("===========================================")

def deposit_screen_and_inputs(username):
  print("=========== Deposit Money ============")
  while True:
    amount = input("Amount to deposit(press Enter to return menu): ")
    
    if amount == "":
      break

    try:
      amount = float(amount)
    except:
      print("Invalid amount")
      continue
    
    if amount <=0:
      print("Amount must be positive number")
      continue
    elif round(amount,2) != amount:
      print("Amount must have at most 2 decimal places")
      continue
    else:
      depositsAndLimits.Deposit(username,str(amount))
      break

def withdrawal_screen_and_inputs(username):
  print("=========== Withdrawal Money ============")
  while True:
    amount = input("Amount to withdraw (press Enter to return menu): ")
    
    if amount == "":
      break

    try:
      amount = float(amount)
    except:
      print("Invalid amount")
      continue
    
    if amount <=0:
      print("Amount must be positive number")
      continue
    elif round(amount,2) != amount:
      print("Amount must have at most 2 decimal places")
      continue
    else:
      withdrawals.withdrawal(username,str(amount))
      break

def continue_menu(username):
  action = input("Press Enter to continue...")
  main_menu(username)

def main_menu(username):
  print(f"""====================================
  PYTHON BANKING SYSTEM
  ====================================
  Welcome, {username}!
  1. View Account Information
  2. Check Balance
  3. Deposit Money
  4. Withdraw Money
  5. Transfer Money
  6. Transaction History
  7. Daily Limits
  8. Change Password
  9. Logout
  0. Exit
====================================""")
  option=input("Select an option: ")
  match option:
    case "1":
      show_account_info(username)
      continue_menu(username)
    case "2":
      show_account_balance(username)
      continue_menu(username)
    case "3":
      deposit_screen_and_inputs(username)
      continue_menu(username)
    case "4":
      withdrawal_screen_and_inputs(username)
      continue_menu(username)
    case "5":
      print("Transfer Money(Soon)")
      continue_menu(username)
    case "6":
      database = load_database()
      save_database(database)
      transaction_history_service(database, username)
    case "7":
      depositsAndLimits.show_daily_limits(username)
      continue_menu(username)
    case "8":
      change_password(username)
      continue_menu(username)
    case "9":
      authentication()
      continue_menu(username)
    case "0":
      print("Exit")
      print("Goodbye!")
      return
    case _:
      print("Invalid option!")
      continue_menu(username)