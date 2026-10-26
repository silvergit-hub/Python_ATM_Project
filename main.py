import csv
import random

# file links as valuables for easy access
login_data_file = "users.csv"
account_data_file = "accounts.csv"
tranactions_data_file = "transactions.csv"

# Simple login for test
username = input("Enter Username: ")
password = input("Enter Password: ")
balance = input("Enter Balance: ")


# read the file and get the valuables we need
# r - read
with open(login_data_file,"r") as file:
    reader = csv.reader(file)
    rows = list(reader)
    try:
        id = rows[-1][0]
    except:
        id = "000000" 

# save datas in the csv file
# "w" - overwrite
# "a" - add new data to the end
with open(login_data_file,"a", newline="") as file:
    writer = csv.writer(file)
    id = "000000"+str(int(id)+1)
    id = id[len(id)-6:]
    writer.writerow([id,username,password])
