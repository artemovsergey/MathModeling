import numpy as np

from view import *


def method_jordan_gauss(matrix, accuracy_print, name_matrix, name_unknown):
    if np.linalg.det(np.array([row[:-1] for row in matrix], dtype=float)) == 0:
        print("det({0}) = 0\n".format(name_matrix))
        return

    for k in range(0, len(matrix)):
        print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

        for j in range(k + 1, len(matrix)):
            c = matrix[j][k] / matrix[k][k]
            for i in range(k, len(matrix[0])):
                matrix[j][i] = matrix[j][i] - c * matrix[k][i]

            print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

        matrix[k] = [elem / matrix[k][k] for elem in matrix[k]]

    for k in range(len(matrix)-1, -1, -1):
        print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

        for j in range(k-1, -1, -1):
            c = matrix[j][k]
            for i in range(k, len(matrix[0])):
                matrix[j][i] = matrix[j][i] - c * matrix[k][i]

            print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    x = [row.pop() for row in matrix]
    print_vector(x, name_unknown, accuracy_print)

    return x


def method_gauss_select_main_element(matrix, accuracy_print, name_matrix, name_unknown):
    if np.linalg.det(np.array([row[:-1] for row in matrix], dtype=float)) == 0:
        print("det({0}) = 0\n".format(name_matrix))
        return

    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    for k in range(0, len(matrix)):
        list_tmp = [abs(matrix[i][k]) for i in range(k, len(matrix))]
        index = list_tmp.index(max(list_tmp)) + k
        matrix[k], matrix[index] = matrix[index], matrix[k]

        print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

        for j in range(k+1, len(matrix)):
            c = matrix[j][k] / matrix[k][k]
            for i in range(k, len(matrix[0])):
                matrix[j][i] = matrix[j][i] - c * matrix[k][i]

            print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    x = list()
    for k in range(len(matrix) - 1, -1, -1):
        x.append((matrix[k][len(matrix[0])-1] - sum([matrix[k][j] * x[len(matrix) - j - 1] for
                                                     j in range(k + 1, len(matrix))])) / matrix[k][k])

    x.reverse()
    print_vector(x, name_unknown, accuracy_print)

    return x
