import pickle

db_file = "customer_db.pickle"

def save_db(customer_db):
    with open(db_file, "wb") as file:
        pickle.dump(customer_db, file)

def load_db():
    try:
        with open(db_file, "rb") as file:
            return pickle.load(file)
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