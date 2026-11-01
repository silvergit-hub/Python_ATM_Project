users={
    "user01": "Test@123",
    "user02": "Test@456",
    "user03": "Test@789"
}
import time 

attempts=0
total_attempts=0
while True:
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    if username in users and users[username]==password:
        print("Login successful!")
        print("Welcome,", username)
        break
    else:
        attempts+=1
        total_attempts+=1   
        print("Invalid username or password!")
        print("Attempts left:", 3-attempts)
        if total_attempts==6:
            print("Your account is permanently blocked.")
            break
        if attempts==3:
            print("Account temporarily locked. Please try again after 60 seconds.")
            for seconds in range(60, 0, -1):
                print(f"Time left: {seconds} seconds")
                time.sleep(1)
            attempts=0