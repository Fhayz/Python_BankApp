from db import load_db, deposit_to_account, reset_customer_password

customer_db = load_db()


def deposit_money(account_number, amount):
    deposit_to_account(customer_db, account_number, amount)


def reset_customer_password_by_agent(account_number, new_password):
    reset_customer_password(customer_db, account_number, new_password)


# Example usage:

deposit_money("123456", 100)  # Deposit $100 to account "123456"
reset_customer_password_by_agent("123456", "newpassword")  # Reset password for account "123456"
