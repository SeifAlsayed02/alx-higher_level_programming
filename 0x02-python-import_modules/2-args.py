#!/usr/bin/python3s
if __name__ == '__main__':
    import sys
    args = sys.argv
    arg_len = len(args)
    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
    for i in range(1, arg_len+1):
        print("{}: {}".format(i, sys.argv[i]))
