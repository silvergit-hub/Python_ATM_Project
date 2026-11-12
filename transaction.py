import storage

user_data_file = "data/users.json"

def digit(number):
    length_of_number=len(str(number))
    number_str="0"*(4-length_of_number)+str(number)
    return number_str

def transaction_history_service(database,user_name):
    user_his_line=next((user for user in database if user.get("username")==user_name),None)
    order=0
    if not user_his_line:
        print("Error")
    else:
        history_line_string=user_his_line.get("transaction_dates")
        history_array=history_line_string.split(",")
        for line in history_array:
            if line !="":
                one_line=line.split("/")
                order+=1
                order_str=digit(order)
                print("ID: TXN"+order_str)
                for part in one_line:
                    print(part)
