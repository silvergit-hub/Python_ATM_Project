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
        attempts=0
        total_attempts=0
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

def change_password(username):
    old_password=input("Enter your current password: ")
    if users[username]!=old_password:
        print("Incorrect current password!")
        return
    new_password=input("Enter your new password: ")
    if new_password==old_password:
        print("New password must be different!")
        return
    if len (new_password)<8:
        print("Password must have at least 8 characters!")
        return
    if not any (char.isupper() for char in new_password):
        print("Password must contain an uppercase letter!")
        return
    if not any (char.islower() for char in new_password):
        print("Password must contain a lowercase letter!")
        return
    if not any (char.isdigit() for char in new_password):
        print("Password must contain a number!")
        return 
    confirm_password=input("Confirm your new password: ")
    if new_password==confirm_password:
        users[username]=new_password
        print("Password changed successfully!")
    else:
        print("Passwords don't match!")