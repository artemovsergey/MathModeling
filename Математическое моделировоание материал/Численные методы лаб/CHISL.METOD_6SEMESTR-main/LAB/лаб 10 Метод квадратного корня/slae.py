import numpy as np
import math

from view import *

def method_square_root(matrix, accuracy_print, name_matrix, name_unknown):
    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    f, s = [row.pop() for row in matrix], np.zeros((len(matrix), len(matrix)))

    det_list = [np.linalg.det(np.array(matrix, dtype=float))]

    if det_list[0] == 0 :
        print("det({0}) = 0\n".format(name_matrix))
        return

    matrix_minor = lambda arr, row, column: np.delete(np.delete(arr, row, axis=0), column, axis=1)

    for i in range(0, len(matrix)-1):
        tmp = [j for j in range(i+1, len(matrix))]
        det_list.append(np.linalg.det(matrix_minor(np.array(matrix, dtype=float), tmp, tmp)))

    def check_major_minor(determinants):
        for det in determinants:
            if det <= 0:
                return False
        return True

    if not check_major_minor(det_list):
        print("One of the major minors <= 0")
        return

    s[0][0] = math.sqrt(matrix[0][0])
    for j in range(1, len(matrix)):
        s[0][j] = matrix[0][j] / s[0][0]
    for i in range(1, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                s[i][i] = math.sqrt(matrix[i][i] - sum([s[k][i] ** 2 for k in range(0, i)]))
            elif i < j:
                s[i][j] = (matrix[i][j] - sum([s[k][i] * s[k][j] for k in range(0, i)])) / s[i][i]

    print_matrix(s, "Matrix S", accuracy_print)

    transpose_s = np.transpose(s)
    print_matrix(transpose_s, "Matrix S(T)", accuracy_print)

    transpose_s = np.column_stack((transpose_s, f))
    print_matrix(transpose_s, "Matrix S(T)'", accuracy_print)

    y = list()
    for k in range(0, len(transpose_s)):
        y.append((transpose_s[k][len(transpose_s[0]) - 1] - sum([transpose_s[k][j] * y[j] for
                                                         j in range(0, k)])) / transpose_s[k][k])
    print_vector(y, "y", accuracy_print)

    s = np.column_stack((s, y))
    print_matrix(s, "Matrix S'", accuracy_print)

    x = list()
    for k in range(len(s) - 1, -1, -1):
        x.append((s[k][len(s[0]) - 1] - sum([s[k][j] * x[len(s) - j - 1] for j in range(k + 1, len(s))])) / s[k][k])

    x.reverse()
    print_vector(x, name_unknown, accuracy_print)

    return x
