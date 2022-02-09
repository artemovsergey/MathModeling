import numpy as np

from view import *
from decimal import Decimal


def method_gauss(matrix, accuracy_print, name_matrix, name_unknown):
    if np.linalg.matrix_rank(np.array(matrix, dtype=float)) != np.linalg.matrix_rank(np.array([row[:-1] for row in
                                                                                               matrix], dtype=float)):
        print("No solutions\n")
        return

    k, basic_solution = 0, False
    while k < len(matrix):
        for j in range(k+1, len(matrix)):
            print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

            if matrix[k][k] == 0:
                flag = False

                for i in range(j, len(matrix)):
                    if matrix[i][k] != 0:
                        flag = True
                        matrix[k], matrix[i] = matrix[i], matrix[k]
                        break

                if flag:
                    k -= 1
                else:
                    basic_solution = True
                break

            c = matrix[j][k] / matrix[k][k]
            for i in range(k, len(matrix[0])):
                matrix[j][i] = matrix[j][i] - c * matrix[k][i]

        k += 1

    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    if basic_solution:
        set_free = set(i for i in range(0, len(matrix)) if matrix[i][i] == 0)

        print("Free variables: " + ", ".join((name_unknown + str(elem+1) for elem in set_free)))

        for elem in list({i for i in range(0, len(matrix))}.difference(set_free))[::-1]:
            out_str = "{0}{1!s} = {2!s}".format(name_unknown, elem + 1, matrix[elem][len(matrix[0]) - 1]
                                                / matrix[elem][elem])

            for var in set_free:
                out_str += " - ({0!s}) * {1}{2!s}".format(matrix[elem][var] / matrix[elem][elem],
                                                          name_unknown, var + 1)

            set_free.add(elem)
            print(out_str)
        print()
    else:
        x = list()
        for k in range(len(matrix) - 1, -1, -1):
            x.append((matrix[k][len(matrix[0])-1] - sum([matrix[k][j] * x[len(matrix) - j - 1] for
                                                         j in range(k + 1, len(matrix))])) / matrix[k][k])

        x.reverse()
        for i, elem in enumerate(x, 1):
            print("{0}{1} = {2}".format(name_unknown, i, round(elem, accuracy_print)))
        print()

        return x


def method_lu_decomposition(matrix, accuracy_print, name_matrix):
    print_matrix(matrix, "Matrix {0}".format(name_matrix), accuracy_print)

    f, l, u = [row.pop() for row in matrix], np.zeros((len(matrix), len(matrix)), dtype=Decimal), np.zeros(
        (len(matrix), len(matrix)), dtype=Decimal)
    
    if len(matrix) != len(matrix[0]):
        print("Matrix {0} not quadratic".format(name_matrix))
        return

    if np.linalg.det(np.array(matrix, dtype=float)) == 0:
        print("det({0}) = 0".format(name_matrix))
        return

    for i in range(0, len(matrix)):
        u[i][i] = Decimal("1")
        for k in range(0, len(matrix)):
            if k <= i:
                l[i][k] = matrix[i][k] - sum([l[i][j] * u[j][k] for j in range(0, k)])
            else:
                u[i][k] = (matrix[i][k] - sum([l[i][j] * u[j][k] for j in range(0, i)])) / l[i][i]

    print_matrix(l, "Matrix L", accuracy_print)
    print_matrix(u, "Matrix U", accuracy_print)

    method_gauss(np.column_stack((u, method_gauss(np.column_stack((l, f)), accuracy_print, "L'", "g"))),
                 accuracy_print, "U'", "x")
