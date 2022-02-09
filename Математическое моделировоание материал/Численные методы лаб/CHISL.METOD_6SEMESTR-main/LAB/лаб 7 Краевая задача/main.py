import data as dat

from boundary_problem import *
from generate import *
from view import *
from plotgraphs import show_graph

with open('output-data.txt', 'w') as f:
    if dat.H <= 0:
        print('Error H>0', file=f)
        exit()

    if dat.ACCURACY < 1:
        print('Error ACCURACY>=1', file=f)
        exit()

    if dat.INTERVAL[0] >= dat.INTERVAL[1]:
        print('Incorrect INTERVAL', file=f)
        exit()

    print('Input data:', file=f)
    print_constants(**{'X0': dat.INTERVAL[0], 'Xn': dat.INTERVAL[1], 'h': dat.H, 'a1': dat.A1, 'a2': dat.A2,
                       'b1': dat.B1, 'b2': dat.B2, 'g1': dat.G1, 'g2': dat.G2}, file=f)
    print(file=f)

    print('Output data:', file=f)
    xi = getRange(dat.INTERVAL[0], dat.INTERVAL[1], dat.H, dat.ACCURACY)
    y_exact = [dat.FUNC_EXACT(x) for x in xi]

    print('Method reduction', file=f)
    yi_reduction = method_reduction(dat.H, xi, (dat.FUNC_DER_Y012, dat.FUNC_DER_S0, dat.FUNC_DER_S12),
                                    dat.A1, dat.A2, dat.B1, dat.B2, dat.G1, dat.G2, file=f)
    print_table(['x', 'y(x)', 'y(exact)', 'inaccuracy'], getData((xi, yi_reduction, y_exact,
                                                list(map(lambda y1, y2: abs(y1 - y2), y_exact, yi_reduction)))), file=f)

    print('\nMethod grid', file=f)
    yi_grid = method_grid(dat.H, xi, dat.FUNC_G, dat.FUNC_F, dat.FUNC_P, dat.A1, dat.A2, dat.B1, dat.B2, dat.G1, dat.G2)
    print_table(['x', 'y(x)', 'y(exact)', 'inaccuracy'],
                getData((xi, yi_grid, y_exact, list(map(lambda y1, y2: abs(y1 - y2), y_exact, yi_grid)))), file=f)

    show_graph({'y(x)': xi, 'y(reduction)': xi, 'y(grid)': xi},
               {'y(x)': y_exact, 'y(reduction)': yi_reduction, 'y(grid)': yi_grid},
               {'y(x)': 'blue', 'y(reduction)': 'red', 'y(grid)': 'green'})
