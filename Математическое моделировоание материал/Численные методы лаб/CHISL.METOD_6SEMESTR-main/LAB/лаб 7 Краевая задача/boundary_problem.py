import numpy as np

from view import *


def runge_kutta_2_method(func1, func2, h, xi, y0, z0):
    const, yi, zi = h / 2, [y0], [z0]
    for i in range(0, len(xi) - 1):
        k1 = func1(xi[i], yi[i], zi[i])
        l1 = func2(xi[i], yi[i], zi[i])
        k2 = func1(xi[i] + const, yi[i] + const * k1, zi[i] + const * l1)
        l2 = func2(xi[i] + const, yi[i] + const * k1, zi[i] + const * l1)
        k3 = func1(xi[i] + const, yi[i] + const * k2, zi[i] + const * l2)
        l3 = func2(xi[i] + const, yi[i] + const * k2, zi[i] + const * l2)
        k4 = func1(xi[i] + h, yi[i] + h * k3, zi[i] + h * l3)
        l4 = func2(xi[i] + h, yi[i] + h * k3, zi[i] + h * l3)
        yi.append(yi[i] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4))
        zi.append(zi[i] + (1 / 6) * h * (l1 + 2 * l2 + 2 * l3 + l4))
    return yi, zi


def method_reduction(h, xi, functions, a1, a2, b1, b2, g1, g2, file=sys.stdout):
    y0, s0 = runge_kutta_2_method(functions[0], functions[1], h, xi, 0, 0)
    y1, s1 = runge_kutta_2_method(functions[0], functions[2], h, xi, 1, 0)
    y2, s2 = runge_kutta_2_method(functions[0], functions[2], h, xi, 0, 1)

    print_table(['x', 'y0', 's0', 'y1', 's1', 'y2', 's2'], getData((xi, y0, s0, y1, s1, y2, s2)), file=file)

    c1, c2 = np.linalg.solve([[a1, b1], [a2 * y1[-1] + b2 * s1[-1], a2 * y2[-1] + b2 * s2[-1]]],
                             [g1, g2 - a2 * y0[-1] - b2 * s0[-1]])

    print('c1 = {0}, c2 = {1}'.format(c1, c2), file=file)

    return [y0[i] + c1 * y1[i] + c2 * y2[i] for i in range(0, len(xi))]


def method_grid(h, xi, func_g, func_f, func_p, a1, a2, b1, b2, g1, g2):
    vector_b = [g1, g2]
    const1, const2, line_zeros = (b1/h), (b2/h), [0 for _ in range(0, len(xi)-2)]
    matrix_a = [[a1-const1, const1] + line_zeros, line_zeros + [-const2, a2+const2]]
    const1, const2 = (h / 2), round((h ** 2), 2)

    for i in range(1, len(xi) - 1):
        row = [0 for _ in range(0, len(xi) - 3)]
        row.insert(i-1, 1 - const1 * func_p(xi[i]))
        row.insert(i, -2 + const2 * func_g(xi[i]))
        row.insert(i+1, 1 + const1 * func_p(xi[i]))
        matrix_a.insert(-1, row)
        vector_b.insert(-1, const2 * func_f(xi[i]))

    return np.linalg.solve(matrix_a, vector_b)
