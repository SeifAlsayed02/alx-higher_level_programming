#!/usr/bin/python3
def print_last_digit(number):
    lst_dgt = abs(number) % 10
    print("{}".format(lst_dgt), end="")
    return lst_dgt
