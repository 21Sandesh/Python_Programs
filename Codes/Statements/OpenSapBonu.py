def encrypt(t, s):
    d = ""
    for c in t:
        if 97 <= ord(c) < 122:
            i = ord(c) + s
            if i > 122:
                i -= 26
            d += chr(i)
        else:
            d += c
    return d



if input("Please enter the number of places to shift:") == input().isdecimal():
    c = int(input())
    if 0 <= c < 26:
        b = input("Please enter a sentence:").lower()
        print(encrypt(b, c))
    else:
        print("You need to enter a number between 0 and 25!")
else:
    print("error")
    c = 0