import json

def load_database():
    with open("history.json","r") as f:
        return json.load(f)

def save_database(database):
    with open("history.json","w") as f:
        json.dump(database, f, indent=4)