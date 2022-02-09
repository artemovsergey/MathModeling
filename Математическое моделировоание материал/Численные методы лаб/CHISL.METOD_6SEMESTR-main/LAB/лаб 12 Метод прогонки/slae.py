import numpy as np

from view import *


def method_run_through(matrix, name_matrix, name_unknown):
    print_matrix(matrix, "Matrix {0}".format(name_matrix))

    fi, bi, ci, ai = [row.pop() for row in matrix], [matrix[i][i] for i in range(0, len(matrix))],\
                     [matrix[i][i+1] for i in range(0, len(matrix)-1)], [matrix[i][i-1] for i in range(1, len(matrix))]

    if np.linalg.det(np.array(matrix, dtype=float)) == 0:
        print("det({0}) = 0\n".format(name_matrix))
        return

    if len(matrix) < 3:
        print("len({0}) < 3\n".format(name_matrix))
        return

    Ai, Bi = [- ci[0] / bi[0]], [fi[0] / bi[0]]
    for i in range(1, len(matrix)-1):
        denominator = ai[i-1] * Ai[i-1] + bi[i]
        Ai.append(-ci[i] / denominator)
        Bi.append((fi[i] - ai[i-1] * Bi[i-1]) / denominator)

    for key, val in {"f": (fi, 1), "a": (ai, 2), "b": (bi, 1), "c": (ci, 1), "A": (Ai, 1), "B": (Bi, 1)}.items():
        print_vector(val[0], key, val[1])

    xi = [(fi[len(fi)-1] - ai[len(ai)-1] * Bi[len(Bi)-1])
          / (bi[len(bi)-1] + ai[len(ai)-1] * Ai[len(Ai)-1])]
    for i in range(len(Ai)-1, -1, -1):
        xi.insert(0, Ai[i]*xi[0] + Bi[i])

    print_vector(xi, name_unknown)

    return xi
