#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        temp = ord(str[i])
        if temp <= 122 and temp >= 97:
            temp = temp - 32
        print("{}".format(chr(temp)), end="")
    print()
