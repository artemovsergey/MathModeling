from view import *

import numpy as np


def method_relaxation(matrix, w, e, name_matrix, name_unknown):
    print_matrix(matrix, "Matrix {0}".format(name_matrix))

    f = [row.pop() for row in matrix]

    if (np.array(matrix).transpose() == np.array(matrix)).all() and np.all(np.linalg.eigvals(matrix) > 0) and 0 < w < 2:
        B, g = np.array([[-matrix[i][j] / matrix[i][i] if i != j else 0 for j in range(0, len(matrix))] for i in
                         range(0, len(matrix))]), [f[i] / matrix[i][i] for i in range(0, len(matrix))]

        x_prev, num_iter = list(g), 0
        while True:
            x_next = list()
            for i in range(0, len(matrix)):
                x_next.append((1 - w) * x_prev[i] + w * (sum([B[i][j] * x_next[j] for j in range(0, i)]) + sum(
                    [B[i][j] * x_prev[j] for j in range(i, len(matrix))]) + g[i]))
            num_iter += 1

            if max([abs(elem - x_prev[i]) for i, elem in enumerate(x_next)]) <= e:
                break

            x_prev = x_next

        print_vector(x_next, name_unknown)
        print("Number of iterations: {0}\n".format(num_iter))

        return x_next
    else:
        print("The second sufficient sign of convergence does not hold")
        return


def method_rapid_descent(matrix, e, name_matrix, name_unknown):
    print_matrix(matrix, "Matrix {0}".format(name_matrix))

    f = [row.pop() for row in matrix]

    if np.linalg.det(np.array(matrix, dtype=float)) == 0:
        print("det({0}) = 0\n".format(name_matrix))
        return

    if len(matrix) < 3:
        print("len({0}) < 3\n".format(name_matrix))
        return

    x_prev, num_iter = np.zeros(len(matrix)), 0
    while True:
        r = np.array(matrix).dot(x_prev) - f
        x_next = x_prev - (np.dot(r, r) / np.dot(np.array(matrix).dot(r), r)) * r
        num_iter += 1

        if max([abs(elem - x_prev[i]) for i, elem in enumerate(x_next)]) <= e:
            break

        x_prev = x_next

    print_vector(x_next, name_unknown)
    print("Number of iterations: {0}\n".format(num_iter))

    return x_next
