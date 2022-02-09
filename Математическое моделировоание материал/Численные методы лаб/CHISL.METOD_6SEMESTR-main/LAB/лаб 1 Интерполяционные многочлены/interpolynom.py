import math


def lagrange(n, xi, yi, x):  # Ln
    polynomial = 0
    for i in range(0, n + 1):
        top_num = 1
        low_num = 1
        for j in range(0, n + 1):
            if j != i:
                top_num *= (x - xi[j])
                low_num *= xi[i] - xi[j]
        polynomial += yi[i] * top_num / low_num
    return polynomial


def split_difference(yi, xi, *argv):
    if len(argv) == 2:
        return (yi[argv[1]] - yi[argv[0]]) / (xi[1] - xi[0])
    return (split_difference(yi, xi, *[i for i in argv if i != argv[0]])
            - split_difference(yi, xi, *[i for i in argv if i != argv[len(argv) - 1]])) / (
                   xi[argv[len(argv) - 1]] - xi[argv[0]])


def residual_term(x0, xi, n, func):  # Rn
    w = 1
    for x in xi:
        w *= abs(x0 - x)
    return (func(xi[0], xi[len(xi) - 1], n) / math.factorial(n + 1)) * w


def newton(n, xi, yi, x):  # Nn
    polynomial = yi[0]
    for i in range(1, n + 1):
        tip = 1
        for j in range(0, i):
            tip *= (x - xi[j])
        polynomial += split_difference(yi, xi, *[k for k in range(0, i + 1)]) * tip
    return polynomial
