import json

with open("history.json","r") as f:
    database=json.load(f)
with open("history.json","w") as f:
    json.dump(database,f,indent=4)
def digit(number):
    length_of_number=len(str(number))
    number_str="0"*(4-length_of_number)+str(number)
    return number_str
history_list=database["history"]
user_name="user01"
user_his_line=next((user for user in history_list if user.get("username")==user_name),None)
order=0
if not user_his_line:
    print("Error")
else:
    history_line_string=user_his_line.get("history_line")
    history_array=history_line_string.split(",")
    for line in history_array:
        one_line=line.split("/")
        order+=1
        order_str=digit(order)
        print("ID: TXN"+order_str)
        for part in one_line:
            print(part)


"""History hissəsində historyşjson faylı doldurulmalı , cari istifadəçinin username main.py kodundakı user_name hissəsinə yazılmalıdır.
history.json faylında yeni tarixçə əlavə edən zaman hər fərqli əməliyyat tarixçəsi vergüllə, içərisindəki elementlər isə (məsələn: Recipient , Type) "/" işarəsi ilə ayrıllamlıdır.
"""