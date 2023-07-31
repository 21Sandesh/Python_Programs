a = input()
b = a.lower()
#b = a.split()
#c = b.split()
for char in b:
    if ord(char) < 97 or ord(char) > 122:
        print(char, end="")
    elif ord(char) == 32:
        print(" ", end="")
    elif 97 <= ord(char) < 118:
        ascii = ord(char)
        inc = ascii + 5
        rev = chr(inc)
        print(",".join(rev), end="")
    elif 122 >= ord(char) >= 118:
        inc = ord(char) - 21
        rev = chr(inc)
        print(",".join(rev), end="")
