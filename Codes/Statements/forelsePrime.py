number = int(input())
for x in range(2,(number/2)):
    if((number%x) == 0):
        print("Number is Prime")
    else:
        print("Number is Not prime")
else:
    print("Number is Not Prime")
        