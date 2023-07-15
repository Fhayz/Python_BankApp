import random
from db import load_db, get_customer, add_customer, make_transfer, save_db


customer_db = load_db()


def create_account():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    DOB = input("Enter Date of Birth (YYYY-MM-DD): ")
    account_number = str(random.randint(100000, 999999))
    while get_customer(customer_db, account_number):
        account_number = str(random.randint(100000, 999999))
    add_customer(customer_db, account_number, username, password, DOB)
    print(f"Account created successfully. Account Number: {account_number}")


def deposit():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    amount = float(input("Enter the deposit amount: "))
    customer = get_customer(customer_db, account_number)
    if customer:
        if customer["password"] != password:
            print("Invalid password.")
        else:
            customer["balance"] += amount
            print(f"Deposit successful. New balance: {customer['balance']}")
            save_db(customer_db)
    else:
        print("Account not found.")


def view_account_info():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    customer = get_customer(customer_db, account_number)
    if customer:
        if customer["password"] != password:
            print("Invalid password.")
        else:
            print(f"Account Number: {account_number}")
            print(f"Username: {customer['username']}")
            print(f"Balance: {customer['balance']}")
    else:
        print("Account not found.")


def make_transfer():
    sender_account = input("Enter your account number: ")
    password = input("Enter your password: ")
    receiver_account = input("Enter the recipient's account number: ")
    amount = float(input("Enter the transfer amount: "))
    customer = get_customer(customer_db, sender_account)
    if customer:
        if customer["password"] != password:
            print("Invalid password.")
        elif customer["balance"] < amount:
            print("Insufficient balance.")
        else:
            make_transfer_to_account(sender_account, receiver_account, amount)
    else:
        print("Account not found.")



def reset_password():
    account_number = input("Enter your account number: ")
    customer = get_customer(customer_db, account_number)
    if customer:
        option = input("Choose an option:\n1. Remember old password\n2. Complete remaining part of your name\n")
        if option == "1":
            password = input("Enter your old password: ")
            if customer["password"] == password:
                new_password = input("Enter your new password: ")
                customer["password"] = new_password
                print("Password reset successful.")
                save_db(customer_db)
            else:
                print("Invalid password.")
        elif option == "2":
            remaining_name = input("Enter the remaining part of your name: ")
            if customer["username"].endswith(remaining_name):
                new_password = input("Enter your new password: ")
                customer["password"] = new_password
                print("Password reset successful.")
                save_db(customer_db)
            else:
                print("Invalid name.")
        else:
            print("Invalid option.")
    else:
        print("Account not found.")


def make_transfer_to_account(sender_account, receiver_account, amount):
    make_transfer(customer_db, sender_account, receiver_account, amount)


def show_menu():
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. View account info")
        print("4. Make Transfer")
        print("5. Reset Password")
        print("6. Exit")

        choice = input("Welcome!! What do you want to do today: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            view_account_info()
        elif choice == "4":
            make_transfer()
        elif choice == "5":
            reset_password()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_menu()
