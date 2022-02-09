import data as dat
import numpy as np

from diffequation import *
from view import print_tables

if dat.H <= 0:
    exit('Error H>0')

if dat.INTERVAL[0] >= dat.INTERVAL[1]:
    exit('Incorrectly set INTERVAL')


xi = [round(x, dat.ACCURACY) for x in np.arange(dat.INTERVAL[0], dat.INTERVAL[1] + dat.H, dat.H)]
list_yi = [euler_method(dat.FUNC, dat.H, xi, dat.F0), midpoint_method(dat.FUNC, dat.H, xi, dat.F0),
           trapezoid_method(dat.FUNC, dat.H, xi, dat.F0), runge_kutta_method(dat.FUNC, dat.H, xi, dat.F0)]
y_exact = [dat.FUNC_EXACT(x) for x in xi]
list_inaccuracy = [[abs(y-y_exact[j]) for j, y in enumerate(yi)] for yi in list_yi]

list_x = [round(x, dat.ACCURACY1) for x in np.arange(dat.INTERVAL1[0], dat.INTERVAL1[1] + dat.H1, dat.H1)]
list_y, list_z = runge_kutta_2_method(dat.FUNC1, dat.FUNC2, dat.H1, list_x, dat.Y0, dat.Z0)
list_y_exact = [dat.FUNC_EXACT1(x) for x in list_x]
inaccuracy = [abs(y-list_y_exact[i]) for i, y in enumerate(list_y)]
methods, names_columns = ('Euler method', 'Midpoint method', 'Trapezoid method', 'Runge-Kutta method',
                          'Runge-Kutta method 2'), ['xi', 'yi', 'y(exact)', 'inaccuracy']

print_tables({method: [names_columns if i != len(methods)-1 else ('xi', 'yi', 'zi', 'y(exact)', 'inaccuracy'),
                       (xi, list_yi[i], y_exact, list_inaccuracy[i]) if i != len(methods)-1 else (list_x,
                        list_y, list_z, list_y_exact, inaccuracy)] for i, method in enumerate(methods)}, '1020x600')
