import random
import os
import bcrypt
import mysql.connector as conn
from dotenv import load_dotenv

load_dotenv("conn.env")
connect = conn.connect(host=os.getenv("db_host"),
                       port=3306,
                       user=os.getenv("db_user"),
                       password=os.getenv("db_password"),
                       database=os.getenv("db_base"))
cursor = connect.cursor()
check = input("Do you want to play the game? (yes/no): ")


def hashing(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if check.lower() == "yes":
    user_exist = input("Do you have an account? (yes/no): ")
    if user_exist.lower() == "yes":
        while True:
            id = input("Enter your ID: ")
            password = input("Enter your password: ")
            cursor.execute("SELECT * FROM record WHERE id=%s", (id, ))
            result = cursor.fetchone()
            if result and check_password(password, result[3].encode('utf-8')):
                print("Login successful!")
                user_name = result[1]
                user_score = result[2]
                print(
                    f"Welcome back, {user_name}! Your current score is {user_score}."
                )
                print("Let's start the game!")
                while True:
                    user_choice = input(
                        "Enter your choice (rock/paper/scissors): \n want to exits(write exit): "
                    ).strip().lower()
                    if user_choice == "exit":
                        print("thank you for playing the game!")
                        break
                    if not (user_choice in ["rock", "paper", "scissors"]):
                        print(
                            "Invalid choice. Please enter 'rock', 'paper', or 'scissors'."
                        )
                        continue
                    choices = random.choice(["rock", "paper", "scissors"])
                    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
                        print(
                            f"You chose {user_choice}. The computer chose {choices}."
                        )
                        if user_choice == choices:
                            print("It's a tie!")
                        elif (user_choice == "rock" and choices == "scissors"
                              ) or (user_choice == "paper" and choices
                                    == "rock") or (user_choice == "scissors"
                                                   and choices == "paper"):
                            print("You win!")
                            user_score += 1
                            print(f"Your current score is {user_score}.")
                            cursor.execute(
                                "UPDATE record SET current_money=%s WHERE id=%s",
                                (user_score, id))
                            connect.commit()
                        else:
                            print("Computer wins!")
                            user_score -= 1
                            print(f"Your current score is {user_score}.")
                            cursor.execute(
                                "UPDATE record SET current_money=%s WHERE id=%s",
                                (user_score, id))
                            connect.commit()
                    else:
                        while True:
                            next_round = input(
                                "want to have a next round? (yes/no): ").strip(
                                ).lower()
                            if next_round == "no":
                                break
                            elif next_round == "yes":
                                break
                            else:
                                print(
                                    "Invalid input. Please enter 'yes' or 'no'."
                                )
                        if next_round == "no":
                            break
                if user_choice == "exit":
                    break
            else:
                print("Invalid ID or password. Please try again.")
    else:
        name = input("Enter your name: ")
        password = input("Create a password: ")
        hashed_password = hashing(password).decode("utf-8")
        while True:
            assigned_id = random.randint(1000, 9999)
            cursor.execute("SELECT * FROM record WHERE id=%s", (assigned_id, ))
            if cursor.fetchone() is None:
                break
        cursor.execute(
            "INSERT INTO record (id, name, password) VALUES (%s, %s, %s)",
            (assigned_id, name, hashed_password))
        connect.commit()
        user_id = assigned_id
        print(
            f"Account created successfully! And Your ID is {user_id}. You can now log in Now."
        )
        while True:
            id = input("Enter your ID: ")
            password = input("Enter your password: ")
            cursor.execute("SELECT * FROM record WHERE id=%s", (id, ))
            result = cursor.fetchone()
            if result and check_password(password, result[3].encode("utf-8")):
                print("Login successful!")
                user_name = result[1]
                user_score = result[2]
                print(
                    f"Welcome back, {user_name}! Your current score is {user_score}."
                )
                print("Let's start the game!")
                while True:
                    user_choice = input(
                        "Enter your choice (rock/paper/scissors): \n want to exits(write exit): "
                    ).strip().lower()
                    choices = random.choice(["rock", "paper", "scissors"])
                    if user_choice == "exit":
                        print('Thank you for playing the game!')
                        break
                    if not (user_choice in ["rock", "paper", "scissors"]):
                        print(
                            "Invalid choice. Please enter 'rock', 'paper', or 'scissors'."
                        )
                        continue
                    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
                        print(
                            f"You chose {user_choice}. The computer chose {choices}."
                        )
                        if user_choice == choices:
                            print("It's a tie!")
                        elif (user_choice == "rock" and choices == "scissors"
                              ) or (user_choice == "paper" and choices
                                    == "rock") or (user_choice == "scissors"
                                                   and choices == "paper"):
                            print("You win!")
                            user_score += 1
                            print(f"Your score is now {user_score}.")
                            cursor.execute(
                                "UPDATE record SET current_money=%s WHERE id=%s",
                                (user_score, id))
                            connect.commit()
                        else:
                            print("Computer wins!")
                            user_score -= 1
                            print(f"Your score is now {user_score}.")
                            cursor.execute(
                                "UPDATE record SET current_money=%s WHERE id=%s",
                                (user_score, id))
                            connect.commit()
                    else:
                        while True:
                            next_round = input(
                                "want to have a next round? (yes/no): ").strip(
                                ).lower()
                            if next_round == "no":
                                break
                            elif next_round == "yes":
                                break
                            else:
                                print(
                                    "Invalid input. Please enter 'yes' or 'no'."
                                )
                        if next_round == "no":
                            break
                if user_choice == "exit":
                    break
            else:
                print("Invalid ID or password. Please try again.")
else:
    print("Maybe next time! Goodbye.")
