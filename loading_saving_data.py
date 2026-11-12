import datetime
from datetime import date
import json
import os

FILENAME="data.json"

def load_data():
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)