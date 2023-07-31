import time
import os

userkey = "Sandesh"
passkey = "3791SandesH"

while(1):

    os.system('cls')

    i = (input("Enter \n 1 To Log In \n 2 To Change Credentials\n --->  "))
    
    if (i == '1'):
        usertemp = input("Username: ")
        if (usertemp.count("s") == 7 and usertemp.count("a") == 3 and usertemp.count("?") == 3 and usertemp.count(">") == 1):
            print(userkey)
            print(passkey)
            time.sleep(1)
            os.system('cls')
            usertemp = input("Username: ")
        
        passtemp = input("Password: ")
        if usertemp == userkey and passtemp == passkey:
            print("Logged in Succefully")
            print('''Whoa, Congrats!!! 
               Now Please Logout
               See You Soon Again''')
            time.sleep(4)
            os.system('cls')
            '''         
            
            
            '''
        if (usertemp != userkey):
            print('''Invalid Username!
                   Try Again''')
            time.sleep(2)

        elif( passtemp != passkey):
            print('''Invalid Password!
                   Try Again''')
            time.sleep(2)
            
        

    if (i == '2'):
        usertemp = input("Username: ")
        if (usertemp.count("s") == 7 and usertemp.count("a") == 3):
            print(userkey)
            print(passkey)
            time.sleep(1)
            os.system('cls')
        
        passtemp = input("Password: ")
        if usertemp == userkey and passtemp == passkey:
            print("Logg in Successfull1")
            time.sleep(1)
            os.system('cls')

            userkey = input("New Username: ")
            passkey = input("New Password: ")
            print("Credentials Changed Successfully!")
            time.sleep(1)
            os.system('cls')
        
        else:
            print("Invliad Credentials!")
            time.sleep(2)
    
    else:
        print("Invalid Input!")
        time.sleep(2)
