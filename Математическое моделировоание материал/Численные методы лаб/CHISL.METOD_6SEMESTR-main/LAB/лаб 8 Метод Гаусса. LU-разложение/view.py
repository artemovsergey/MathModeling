import sys


def print_matrix(matrix, name, accuracy_print, file=sys.stdout):
    print(name, file=file)
    for row in matrix:
        for elem in row:
            print(round(elem, accuracy_print), end=" ", file=file)
        print(file=file)
    print(file=file)
