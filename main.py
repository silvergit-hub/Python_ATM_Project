import datetime
from datetime import date
import json
import os
from loading_saving_data import load_data,save_data
from transfer_part import transfer_part



user_account="user01" #user_account hal-hazırda hesaba giriş edən istifadəçinin hesabıdır

database = load_data()
load_data()
transfer_part(database,user_account)



"""In json file Last_transfer_date have to be filled and current user's username have to be written to user_account in main.py file """