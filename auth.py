import hashlib
import json
import os
import time
Document="users.json"
def load_data():
  if not os.path.exists(Document):
    users = {
        "user1": {
            "password": hashlib.sha256("Test@123".encode()).hexdigest(),
            "attempts": 0,
            "blocked": False,
        },
        "user2": {
            "password": hashlib.sha256("Test@456".encode()).hexdigest(),
            "attempts": 0,
            "blocked": False,
        },
        "user3": {
            "password": hashlib.sha256("Test@789".encode()).hexdigest(),
            "attempts": 0,
            "blocked": False,
        },
    }
    with open(Document, "w") as f:
      json.dump(users, f)
    users
    return users

  with open(Document, "r") as f:
    return json.load(f)


def save_data(data):
  with open(Document, "w") as f:
    json.dump(data, f)