import datetime
from datetime import date
import json
import os

FILENAME="data.json"

def load_data1():
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_data1(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)