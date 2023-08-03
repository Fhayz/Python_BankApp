import json

db_file = "customer_db.json"
log_file = "transaction_log.txt"

def save_db(customer_db):
    with open(db_file, "w") as file:
        json.dump(customer_db, file, indent=2)

def load_db():
    try:
        with open(db_file, "rb") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def get_customer(customer_db, account_number):
    return customer_db.get(account_number)


def add_customer(customer_db, account_number, username, password, DOB, balance=0 ):
    customer_db[account_number] = {
        "username": username,
        "password": password,
        "balance": balance,
        "date_of_birth": DOB,
    }
    save_db(customer_db)

def reset_customer_password(customer_db, account_number, new_password):
    customer = get_customer(customer_db, account_number)
    if customer:
        customer["password"] = new_password
        save_db(customer_db)
        print("Password reset successful.")
    else:
        print("Customer not found.")


def deposit_to_account(customer_db, account_number, amount):
    customer = get_customer(customer_db, account_number)
    if customer:
        customer["balance"] +=amount
        save_db(customer_db)
        print("Deposit successful.")
    else:
        print("Customer not found.")
    save_db(customer_db)


def validate_transfer(customer_db, sender_account, receiver_account, amount):
    sender = get_customer(customer_db, sender_account)
    receiver = get_customer(customer_db, receiver_account)
    if sender and receiver:
        if sender["password"] != input("Enter your password: "):
            print("Invalid password.")
            return False
        if sender["balance"] < amount:
            print("Insufficient balance.")
            return False
        return True
    else:
        print("Invalid account number(s).")
        return False
    

def make_transfer(customer_db, sender_account, receiver_account, amount):
    sender = get_customer(customer_db, sender_account)
    receiver = get_customer(customer_db, receiver_account)
    if validate_transfer(customer_db, sender_account, receiver_account, amount):
        sender["balance"] -= amount
        receiver["balance"] += amount
        save_db(customer_db)
        print("Transfer successful.")
        log_transaction(f"Transferred {amount} from account {sender_account} to account {receiver_account}.")
    save_db(customer_db)

    
def log_transaction(transaction_details):
    try:
        with open(log_file, "a") as file:
            json.dump(transaction_details, file, indent=2)
            file.write("\n")
    except Exception as e:
        print(f"Error while logging transaction: {e}")
if __name__ == "__main__":
    pass