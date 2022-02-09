import numpy as np
import threading

from view import *


def LU_decomposition(matrix, name_matrix, accuracy_print):
    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    l, u = np.zeros((len(matrix), len(matrix)), dtype=float), np.zeros((len(matrix), len(matrix)), dtype=float)

    for i in range(0, len(matrix)):
        u[i][i] = 1
        for k in range(0, len(matrix)):
            if k <= i:
                l[i][k] = matrix[i][k] - sum([l[i][j] * u[j][k] for j in range(0, k)])
            else:
                u[i][k] = (matrix[i][k] - sum([l[i][j] * u[j][k] for j in range(0, i)])) / l[i][i]

    print_matrix(l, "Matrix L", accuracy_print)
    print_matrix(u, "Matrix U", accuracy_print)

    return l, u


def getDet_LU_decomposition(matrix, name_matrix, accuracy_print):
    l, u = LU_decomposition(matrix, name_matrix, accuracy_print)
    return np.linalg.det(l) * np.linalg.det(u)


def getInverseMatrix_LU_decomposition(matrix, name_matrix, accuracy_print):
    l, u = LU_decomposition(matrix, name_matrix, accuracy_print)
    e = np.eye(len(matrix))

    def func1(array, index, result):
        y = list()
        for k in range(0, len(array)):
            y.append((array[k][len(array[0]) - 1] - sum([array[k][j] * y[j] for j in range(0, k)])) / array[k][k])
        result.append((index, y))

    def func2(array, index, result):
        x = list()
        for k in range(len(array) - 1, -1, -1):
            x.append((array[k][len(array[0]) - 1] - sum([array[k][j] * x[len(array) - j - 1] for
                                                         j in range(k + 1, len(array))])))
        x.reverse()
        result.append((index, x))

    def reverseCourse(matrix_a, array_vectors, func, name_unknown, accuracy):
        threads, res = list(), list()

        for i in range(len(array_vectors)):
            thread = threading.Thread(target=func, args=(np.column_stack((matrix_a, array_vectors[i])), i, res))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for i, vector in res:
            print("Vector {0}{1!s}".format(name_unknown.title(), i + 1))
            print_vector(vector, name_unknown, accuracy)

        res.sort(key=lambda elem: elem[0])

        return [elem[1] for elem in res]

    array_x = reverseCourse(u, reverseCourse(l, e, func1, "y", accuracy_print), func2, "x", accuracy_print)
    inverse_matrix = [[row[i] for row in array_x] for i in range(len(matrix))]

    print_matrix(inverse_matrix, "Matrix {0}(-1)".format(name_matrix), accuracy_print)

    return inverse_matrix


def getInverseMatrix_JordanGauss(matrix, name_matrix, accuracy_print):
    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)
    matrix = list(map(lambda row1, row2: list(row1) + list(row2), matrix, np.eye(len(matrix))))

    for k in range(0, len(matrix)):
        print_matrix(matrix, "Matrix {0}|E".format(name_matrix), accuracy_print)

        for j in range(k + 1, len(matrix)):
            c = matrix[j][k] / matrix[k][k]
            for i in range(k, len(matrix[0])):
                matrix[j][i] = matrix[j][i] - c * matrix[k][i]

            print_matrix(matrix, "Matrix {0}|E".format(name_matrix), accuracy_print)

        matrix[k] = [elem / matrix[k][k] for elem in matrix[k]]

    for k in range(len(matrix) - 1, -1, -1):
        print_matrix(matrix, "Matrix {0}|E".format(name_matrix), accuracy_print)

        for j in range(k - 1, -1, -1):
            c = matrix[j][k]
            for i in range(k, len(matrix[0])):
                matrix[j][i] = matrix[j][i] - c * matrix[k][i]

            print_matrix(matrix, "Matrix {0}|E".format(name_matrix), accuracy_print)

    inverse_matrix = [row[len(matrix):]for row in matrix]
    print_matrix(inverse_matrix, "Matrix {0}(-1)".format(name_matrix), accuracy_print)

    return inverse_matrix
