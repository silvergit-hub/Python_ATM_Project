users={
    "user01": "Test@123",
    "user02": "Test@456",
    "user03": "Test@789"
}

attempts=0
while attempts<3:
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    if username in users and users[username]==password:
        print("Login successful!")
        print("Welcome,", username)
        break
    else:
        attempts+=1
        print("Invalid username or password!")
        print("Attempts left:", 3-attempts)