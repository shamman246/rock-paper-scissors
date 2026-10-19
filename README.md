# 🎮 Rock Paper Scissors

A command-line Rock-Paper-Scissors game built with Python and MySQL. The project includes user registration, login authentication, bcrypt password hashing, and persistent score tracking.

## ✨ Features

- **User Registration:** Create an account with a randomly assigned user ID.
- **Login System:** Authenticate users using their ID and password.
- **Password Security:** Hash passwords using bcrypt instead of storing plain-text passwords.
- **MySQL Integration:** Store user information and scores in a database.
- **Score Tracking:** Update and save scores after each round.
- **Interactive Gameplay:** Play Rock, Paper, or Scissors against the computer.

## 🛠️ Technologies Used

- Python
- MySQL
- `mysql-connector-python`
- `bcrypt`
- `python-dotenv`

## 📋 Requirements

Before running the project, install:

- Python 3
- MySQL Server
- Git (optional, for cloning the repository)

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shamman246/rock-paper-scissors.git
cd rock-paper-scissors
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install bcrypt mysql-connector-python python-dotenv
```

### 4. Configure MySQL

Start your MySQL Server and create a database:

```sql
CREATE DATABASE rock_paper_scissors;
USE rock_paper_scissors;
```

Create the user table:

```sql
CREATE TABLE record (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    current_money INT NOT NULL DEFAULT 0
);
```

**Note:** This schema assumes the Python code reads the password from the fourth column using `SELECT *` and stores the score in `current_money`. Make sure your actual table column order matches your code.

### 5. Configure environment variables

Create a local file named `conn.env` in the project directory:

```env
db_host=localhost
db_user=your_mysql_username
db_password=your_mysql_password
db_base=rock_paper_scissors
```

Replace the example values with your own MySQL credentials.

**Never upload `conn.env` or expose your database credentials publicly.**

### 6. Run the game

```bash
python game.py
```

Follow the prompts to create an account or log in and start playing.

## 🔐 Security

- Passwords are hashed using bcrypt.
- Database credentials are loaded from environment variables.
- The `.gitignore` file excludes environment files and the Python virtual environment.

## 📚 What I Learned

- Connecting Python applications to MySQL.
- Performing database queries and updating records.
- Implementing user registration and login.
- Hashing and verifying passwords using bcrypt.
- Managing environment variables with `python-dotenv`.
- Using Git and GitHub for version control.

## 🔮 Future Improvements

- Refactor repeated code into reusable functions.
- Improve input validation and error handling.
- Add a leaderboard.
- Improve database connection management.
- Add automated tests.

## 👨‍💻 Author

**Shamman Ali**

A beginner Python project created to practise programming, database integration, authentication, and version control.
