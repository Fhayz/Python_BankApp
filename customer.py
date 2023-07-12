import sys
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
   
def deposit_to_account(account_number, amount):
    customer = get_customer(customer_db, account_number)
    if customer:
        customer['balance'] += amount
        print(f"Deposit successful. New balance: {customer['balance']}")
        save_db(customer_db)
    else:
        print("Account not found.")


def view_account_info(account_number, password):
    account_number = input("Enter  your Account Number")
    password = input("Enter Password")
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

def deposit_to_account(account_number, amount):
    customer = get_customer(customer_db, account_number)
    if customer:
        customer['balance'] += amount
        print(f"Deposit successful. New balance: {customer['balance']}")
        save_db(customer_db)
    else:
        print("Account not found.")
2


def make_transfer_to_account(sender_account, receiver_account, amount):
    make_transfer(customer_db, sender_account, receiver_account, amount)


def reset_customer_password_by_customer(account_number, password):
    customer = get_customer(customer_db, account_number)
    if customer:
        if customer["password"] != password:
            print("Invalid password.")
        else:
            option = input("Choose an option:\n1. Remember old password\n2. Complete remaining part of your name\n")
            if option == "1":
                new_password = input("Enter your old password: ")
                customer["password"] = new_password
                print("Password reset successful.")
            elif option == "2":
                remaining_name = input("Enter the remaining part of your name: ")
                new_password = password + remaining_name
                customer["password"] = new_password
                print("Password reset successful.")
            else:
                print("Invalid option.")
            save_db(customer_db)
    else:
        print("Account not found.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        create_account()
    elif len(sys.argv) == 3:
        account_number = sys.argv[1]
        password = sys.argv[2]
        view_account_info(account_number, password)
    elif len(sys.argv) == 5:
        sender_account = sys.argv[1]
        receiver_account = sys.argv[2]
        amount = int(sys.argv[3])
        password = sys.argv[4]
        make_transfer_to_account(sender_account, receiver_account, amount)
    elif len(sys.argv) == 6:
        account_number = sys.argv[1]
        password = sys.argv[2]
        reset_customer_password_by_customer(account_number, password)
    else:
        print("Invalid arguments.")

def show_menu():
    while True: 
      print("\nMenu:")
      print("1. Create Account")
      print("2. View account info")
      print("3. Make Transfer")
      print("4. Reset Password")
      print("5. Exit")

      choice = input("Welcome!! What do you want to do today: ")

      if choice == "1":
            create_account()
      elif choice == "2":
            view_account_info()      
      elif choice == "3":
            make_transfer()
      elif choice == "4":
            reset_customer_password_by_customer()
      elif choice == "5":
            print("Exiting the program.")
            break
      else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_menu()