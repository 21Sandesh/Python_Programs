from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Password Manager\key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Password Manager\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Password Manager\passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def delete():
    with open('D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Password Manager\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


    # global accname
    accname = input("Enter the Account Name to be Deleted: ")
    with open('D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Password Manager\passwords.txt', 'a') as f:
        data = f.readline()

    with open('D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Password Manager\passwords.txt', 'a') as f:
        for line in data:
            if line.strip("\n") != accname:
                f.write(line)


while True:
    mode = input(
        '''
        Menu: 
        Enter 1 to View Passwords
        Enter 2 to add New Password
        Enter 3 to Delete Password
        Enter 0 to Quit
        INPUT:  ''')
    if mode == "0":
        break

    if mode == "1":
        view()
    elif mode == "2":
        add()
    elif mode == "3":
        delete()
    else:
        print("Invalid mode.")
        continue