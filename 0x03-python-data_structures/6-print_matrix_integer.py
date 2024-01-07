#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            last = " "
            if (j+1) == len(matrix[i]):
                last = ""
                print("{:d}".format(matrix[i][j]), last=last)
        print()
