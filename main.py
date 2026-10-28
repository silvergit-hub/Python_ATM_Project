from datetime import date
import csv
import os

CSV_FILE = "users.csv"


def save_users_to_csv(users_list):
  fieldnames = [
      "username",
      "password",
      "account_number",
      "balance",
      "status",
      "daily_transfer_count",
      "last_transfer_date",
  ]

  with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() 
    for user in users_list:
      writer.writerow(user) 


def load_users_from_csv():
  """CSV faylından istifadəçi məlumatlarını oxuyur."""
  if not os.path.exists(CSV_FILE):
    return []

  users_list = []
  with open(CSV_FILE, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      row["balance"] = float(row["balance"])
      row["daily_transfer_count"] = int(row["daily_transfer_count"])
      users_list.append(row)

  return users_list
load_users_from_csv()
print("Sender: ")
recipient_account=input("Recipient account: ")
recipient=input("Recipient: ")
amount=input("Amount (AZN): ")
confirm=input("Confirm transfer (Y/N): ")
today_str = date.today().strftime("%Y-%m-%d")
if last_transfer_date!=today_str:
    transfer_count=0
if transfer_count>=5:
    print("You reached daily limits")
    print("Transfer unsuccesfully")
