import sys


def print_matrix(matrix, name, accuracy_print, file=sys.stdout):
    print(name, file=file)
    for row in matrix:
        for elem in row:
            print(round(elem, accuracy_print), end=" ", file=file)
        print(file=file)
    print(file=file)


def print_vector(vector, name_unknown, accuracy_print, file=sys.stdout):
    for i, elem in enumerate(vector, 1):
        print("{0}{1} = {2}".format(name_unknown, i, round(elem, accuracy_print)), file=file)
    print(file=file)
