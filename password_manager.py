from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# checkin for master pw that if it works that it is fine otherwise remove this
master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as file:
        file.write(name + " = " + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("=")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


while True:
    mode = input("Would you like to add a new password or view an existing ones (view / add), press q to quit? ").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")