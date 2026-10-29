import storage

# file links as valuables for easy access
user_data_file = "data/users.json"

storage.create_default_user_data(user_data_file)

# Simple login for test
username = input("Enter Username: ")
password = input("Enter Password: ")
balance = input("Enter Balance: ")

user_list = []
user_list = storage.load_data(user_data_file)
print(user_list)
storage.add_user(user_list,user_data_file,username,password,balance)

