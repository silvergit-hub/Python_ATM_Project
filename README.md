# ATM Bank System

## 1. About the Project

Welcome to our ATM Bank System! 

This project is a simple banking application developed using Python. Its main purpose is to simulate basic banking operations and demonstrate how a real-world ATM system works.

Users can interact with the system to perform different banking operations, manage their accounts, and handle their balance.

**Project Goals:**
- Understand how banking systems work.
- Practice Python programming and problem-solving.
- Learn how to work with files and store data.
- Improve teamwork and collaborative programming skills.

---

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Data storage and management |
| Git & GitHub | Version control and teamwork |

---

## 3. Project Structure

```text
GroupProjectProgramming/
│
├── main.py
├── authentification.py
├── storage.py
├── withdrawals.py
├── depositsAndLimits.py
├── atm.py
├── README.md
└── data/
    ├── atm.json
    └── users.json
```

**File descriptions:**

- `main.py` – Gethers All python files and make them work together
- `authentification.py` – Log in, Sign up, Change password, and Bank System functions work in it
- `storage.py` – Load data, Save data, Default users, Password change, Add New User functions work in it
- `withdrawals.py` – Check and Updates Withdrawals
- `depositsAndLimits.py` – Check and Updates Withdrawals, besides that shows daily limits screen.
- `atm.py` – Updates ATM cash and User daily limits.
- `users.json` - User datas.
- `ATM.json` - ATM datas, limits and daily cash.

---

## 4. How the System Works (Workflow)

### 4.1. Account Management

### 4.2. Data Storage with JSON
We chose JSON as our data storage format because it provides a simple and structured way to store information.

JSON allows us to organize account information into key-value pairs, making it easier to read, access, update, and save user data.

**Our implementation:**
- Account information and ATM information are stored in a JSON files.
- When the program starts, it loads the existing datas.
- After changes are made, the updated information is saved back into the files.

### 4.3. Deposit Operation
[Explain your deposit function.]

**Our workflow:**
1. The user selects the deposit operation.
2. The system gets account infos from the JSON file.
2. The system receives the amount entered by the user.
3. The system validates the amount.
4. The account balance is increased.
5. The updated information is saved to the JSON file.

### 4.4. Withdrawal Operation
In my functions values must be checked before going in the function so in authentification or in other inputs before using fucntion you must check if values are str if it is an amount valueable 

**Our workflow:**
1. The user selects the withdrawal operation.
2. The system receives the requested amount.
3. The system checks whether the amount is valid.
3. - This part wrote before going in function
4. The system gets account infos from the JSON file.
5. The system checks whether the account has sufficient funds.
6. The balance is decreased if the operation is successful.
7. The updated information is saved to the JSON file.

### 4.5. Additional Features
[Describe other features implemented by your teammates.]

---

## 5. Team Contributions

This project was developed collaboratively. Each team member was responsible for different parts of the system.

### Member A – Aydan
- Mainly worked on authentification.
- Wrote login, sign in, password changes and some console interfaces for other users.

### Member B – Sahib
- Mainly worked on data bases (JSON).
- Also wrote withdrawals, deposits, daily limits and some features for ATM.

### Member C – Sücəddin
- Also worked on some part of datas and JSONs.
- Mainly worked on transactions, their savings and checkouts.

---

## 6. How to Run the Project

**Requirements:**
- Python 3.13

**Steps:**

1. Clone the repository:

   ```bash
   git clone https://github.com/silvergit-hub/Python_ATM_Project
   ```

2. Navigate to the project folder:

   ```bash
   cd Python_ATM_Project
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## 7. What We Learned

- Working with Python functions and modules.
- Reading and writing JSON files.
- Managing data and account balances.
- Using Git branches, commits, merges, and pull requests.
- Collaborating on a shared project.

---

## 8. Future Improvements

- We can write an interface for our BankSystem

---

## 9. Conclusion

This project was a valuable experience for our team. Throughout its development, we improved our Python programming skills, learned how to manage data using JSON, and gained practical experience working with Git and GitHub.

Although we faced some challenges, working together helped us find solutions and improve our understanding of software development.

We hope this project shows our effort, teamwork and knowledge gained throughout the process.

---

**Developed with Python by [Team Name]**