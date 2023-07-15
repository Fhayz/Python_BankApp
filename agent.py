from db import load_db, deposit_to_account, reset_customer_password, get_customer

customer_db = load_db()


def deposit_money(account_number, amount):
    customer = get_customer(customer_db, account_number)
    if customer:
        deposit_to_account(customer_db, account_number, amount)
        print(f"Deposit successful. New balance: {customer['balance']}")
    else:
        print("Account not found.")


def reset_customer_password_by_agent(account_number, new_password):
    customer = get_customer(customer_db, account_number)
    if customer:
        reset_customer_password(customer_db, account_number, new_password)
        print("Password reset successful.")
    else:
        print("Account not found.")


def show_menu():
    while True:
        print("\nAgent Menu:")
        print("1. Deposit Money")
        print("2. Reset Customer Password")
        print("3. Exit")

        choice = input("What action do you want to perform: ")

        if choice == "1":
            account_number = input("Enter the customer's account number: ")
            amount = float(input("Enter the amount to deposit: "))
            deposit_money(account_number, amount)
        elif choice == "2":
            account_number = input("Enter the customer's account number: ")
            new_password = input("Enter the new password: ")
            reset_customer_password_by_agent(account_number, new_password)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_menu()
