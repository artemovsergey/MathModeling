from view import *

import numpy as np


def __common_func(func, matrix, e, name_matrix, name_unknown):
    print_matrix(matrix, "Matrix {0}".format(name_matrix))

    f = [row.pop() for row in matrix]

    if np.linalg.det(np.array(matrix, dtype=float)) == 0:
        print("det({0}) = 0\n".format(name_matrix))
        return

    if len(matrix) < 3:
        print("len({0}) < 3\n".format(name_matrix))
        return

    if sum([abs(matrix[i][i]) > matrix[i][j] for i in range(0, len(matrix)) for j in
            range(0, len(matrix)) if i != j]) != (len(matrix) ** 2) - len(matrix):
        print("Matrix {0} does not have a diagonal predominance".format(name_matrix))
        return

    B, g = np.array([[-matrix[i][j] / matrix[i][i] if i != j else 0 for j in range(0, len(matrix))] for i in
                     range(0, len(matrix))]), [f[i] / matrix[i][i] for i in range(0, len(matrix))]

    if max([abs(sum(row)) for row in B]) >= 1:
        print("The sufficient convergence condition is not satisfied")
        return

    x_prev, num_iter = list(g), 0
    while True:
        x_next = func(x_prev, B, g)
        num_iter += 1

        if max([abs(elem - x_prev[i]) for i, elem in enumerate(x_next)]) <= e:
            break

        x_prev = x_next

    print_vector(x_next, name_unknown)
    print("Number of iterations: {0}\n".format(num_iter))

    return x_next


def method_jacobi(matrix, e, name_matrix, name_unknown):
    return __common_func(lambda x_prev, matrix_b, g: matrix_b.dot(x_prev) + g, matrix, e, name_matrix, name_unknown)


def method_seidel(matrix, e, name_matrix, name_unknown):
    def func(x_prev, matrix_b, g):
        x_next = list()
        for i in range(0, len(matrix)):
            x_next.append(sum([matrix_b[i][j] * x_next[j] for j in range(0, i)]) + sum([matrix_b[i][j] * x_prev[j] for
                                                                                 j in range(i, len(matrix))]) + g[i])
        return x_next

    return __common_func(func, matrix, e, name_matrix, name_unknown)
