import click
import time



loginkey = "Sandesh"
passwordkey = "3791SandesH"
key = "qcrnu<p"

while(1):
    click.clear()
    LoginID = input("Enter Login ID:   ")
    if(LoginID == key):
        print(loginkey + "\n" + passwordkey)
        time.sleep(2)
        click.clear()
        LoginID = input("Enter Login ID:   ")
    Password = input("Enter Password:  ")
    if(LoginID == loginkey):
        if(Password == passwordkey):
            print("Login Succesfull !!!")
        else:
            print('''Invalid Password,
            Try Again''')
    else:
        print('''Invalid Credentials,
            Try Again''')
    time.sleep(2)
    click.clear()
