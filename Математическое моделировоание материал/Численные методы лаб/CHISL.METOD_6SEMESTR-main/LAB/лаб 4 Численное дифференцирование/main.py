import data as dat
import numdif as nd
import numpy as np
import sys


def print_table(file=sys.stdout, **d):
    for k in d:
        print('{0}: {1}'.format(k, d[k]), file=file)


def print_result(name, array, a, b, file=sys.stdout):
    print(f'{name}: {array!s} i = {a!s}, ..., {b!s}', file=file)


if dat.X0 >= dat.Xn:
    print('Error Xn>X0')
    exit()

if dat.H <= 0:
    print('Error H>0')
    exit()

if dat.NUM_DECIMAL_PLACES <= 0:
    print('Error NUM_DECIMAL_PLACES>0')
    exit()

print('Input data:')
print_table(X0=dat.X0, Xn=dat.Xn, H=dat.H)
print()

print('Output data:')
xi = [round(x, dat.NUM_DECIMAL_PLACES) for x in np.arange(dat.X0, dat.Xn + dat.H, dat.H)]
yi = [dat.FUNC(x) for x in xi]
print_table(Xi=xi, Yi=yi)
print()

table = {
    'x': xi,
    "y'(x) exact": [dat.FIRST_DER(x) for x in xi],
    "y'(x) left": nd.left_der(yi, dat.H),
    "y'(x) right": nd.right_der(yi, dat.H),
    "y'(x) central": nd.central_der(yi, dat.H),
    'y"(x) exact': [dat.SECOND_DER(x) for x in xi],
    'y"(x) approximate': nd.approximate_second_der(yi, dat.H),
}
n = len(yi) - 1
values = {
    'x': (0, n),
    "y'(x) exact": (0, n),
    "y'(x) left": (1, n),
    "y'(x) right": (0, n - 1),
    "y'(x) central": (1, n - 1),
    'y"(x) exact': (0, n),
    'y"(x) approximate': (1, n - 1),
}

for key in table:
    print_result(key, table[key], values[key][0], values[key][1])
