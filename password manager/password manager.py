from cryptography.fernet import Fernet

'''
#Iniate a key in key.key for encryption
def write_key():
    key =   Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
'''

#Loading key generated in key.key
def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

key = load_key() # Take the key
fer = Fernet(key) #

#Viewing the file for name and password
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user + "\n Password:", fer.decrypt(passw.encode()).decode())
            print("=====================================")

#adding new content into the file
def add():
    name = input("Enter your account name: ")
    pwd = input("Enter your password: ")
    print("Account stored!")
    print("=====================================")

    # a for appending, w to make a new save, r to read
    # \n breaks line
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # first encode into byte and then encrypt with a key


optionList = ["view", "add", "quit"]

while True:
    print("VIEW     ADD     QUIT")
    print("=====================================")
    mode = input("What do you wish to perform? ").lower()
    print("=====================================")

    if mode not in optionList:
        print("Enter a valid option.")
        print("=====================================")
        continue

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    elif mode == "quit":
        break