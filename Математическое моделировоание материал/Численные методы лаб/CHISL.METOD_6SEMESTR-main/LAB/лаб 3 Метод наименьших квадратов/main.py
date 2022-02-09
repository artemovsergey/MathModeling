import data as dat
import leastsquares as ls
import plotgraphs as pg
import config


with open(config.FILE_NAME, 'w') as f:

    if len(dat.X) != len(dat.Y):
        print('Error len(X)==len(Y)', file=f)
        exit()

    print('Input data:', file=f)
    pg.print_table(X=dat.X, Y=dat.Y, file=f)
    print(file=f)

    print('Output data:', file=f)
    func1 = ls.get_function(config.FUNC_1, dat.X, dat.Y, config.x, config.a, config.b)
    func2 = ls.get_function(config.FUNC_2, dat.X, dat.Y, config.x, config.a, config.b, config.c)
    func3 = ls.get_function(config.FUNC_3, dat.X, dat.Y, config.x, config.a, config.b, config.c, config.d)

    for i, func in enumerate([func1, func2, func3]):
        print('f{0}(x) = {1}'.format(i + 1, func), file=f)

    print(file=f)

    for i, func in enumerate([func1, func2, func3]):
        print('||r{0}|| = {1}'.format(i + 1, ls.dev_rate(func, dat.X, dat.Y, config.x)), file=f)

    functions = {
        "y(x)": dat.Y,
        "f1(x)": [func1.subs({config.x: x}) for x in dat.X],
        "f2(x)": [func2.subs({config.x: x}) for x in dat.X],
        "f3(x)": [func3.subs({config.x: x}) for x in dat.X],
    }

    colors = {
        "y(x)": "blue",
        "f1(x)": "black",
        "f2(x)": "green",
        "f3(x)": "red",
    }

pg.show_graph(dat.X, functions, colors)
