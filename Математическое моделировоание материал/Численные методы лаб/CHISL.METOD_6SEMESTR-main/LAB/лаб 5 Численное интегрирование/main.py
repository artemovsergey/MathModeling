import data as dat
import numintegration
import numpy as np
import decimal


def print_table(**d):
    for key in d:
        print('{0}: {1}'.format(key, d[key]))


if dat.INTERVAL[0] >= dat.INTERVAL[1]:
    print('Incorrect integration interval')
    exit()

if dat.N1 <= 0 or dat.N2 <= 0 or dat.N3 > 6 or dat.N3 <= 0:
    print('Incorrect N1, N2, N3')
    exit()

print('Input data:')
print_table(N1=dat.N1, N2=dat.N2, N3=dat.N3)
print('INTERVAL = [{0}, {1}]'.format(float(dat.INTERVAL[0]), float(dat.INTERVAL[1])), end='\n\n')

print('Output data:')
print('Rectangles and trapezoids methods:')
H1 = (dat.INTERVAL[1] - dat.INTERVAL[0]) / decimal.Decimal(dat.N1)
xi = [float(i) for i in np.arange(dat.INTERVAL[0], dat.INTERVAL[1] + H1, H1)]
fi = [dat.INTEGRAND_FUNC(x) for x in xi]

H1, a, b = float(H1), float(dat.INTERVAL[0]), float(dat.INTERVAL[1])

S = dat.PRIMITIVE_FUNC(b) - dat.PRIMITIVE_FUNC(a)

print_table(**{
    'h': H1,
    'x': xi,
    'f(x)': fi,
    'S(left rectangles)': numintegration.left_rectangles(fi, H1),
    'S(right rectangles)': numintegration.right_rectangles(fi, H1),
    'S(central rectangles)': numintegration.central_rectangles(dat.INTEGRAND_FUNC, xi, H1),
    'S(trapezoids)': numintegration.trapezoids(fi, H1),
    'S': S,
})
print()

print('Parabolas method:')
H2 = (dat.INTERVAL[1] - dat.INTERVAL[0]) / (2 * decimal.Decimal(dat.N2))
xi = [float(i) for i in np.arange(dat.INTERVAL[0], dat.INTERVAL[1] + H2, H2)]
fi = [dat.INTEGRAND_FUNC(x) for x in xi]

H2 = float(H2)
print_table(**{
    'h': H2,
    'x': xi,
    'f(x)': fi,
    'S(parabolas)': numintegration.parabolas(fi, H2),
    'S': S,
})
print()

print('Gaussian method:')
Tk = [((b - a) / 2) * numintegration.Xk[i] + ((b + a) / 2) for i in range(0, dat.N3)]
fi = [dat.INTEGRAND_FUNC(t) for t in Tk]

print_table(**{
    'N': dat.N3,
    'Xk': numintegration.Xk[:dat.N3],
    'Tk': Tk,
    'f(Tk)': fi,
    'Ck': numintegration.Ck[:dat.N3],
    'S(gauss)': numintegration.gauss(a, b, fi, dat.N3),
    'S': S,
})
