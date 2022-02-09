import data as dat
import plotgraphs as pg
import interpolynom as ip


def selection(list_x, t, n):
    for index, elem in enumerate(list_x):
        if t < elem:
            if index - n < 0:
                return list_x[:index + abs(index - n - 1)]
            else:
                return list_x[index - n:index + 1]
    return list_x[len(list_x) - (n + 1):]


with open('output-data.txt', 'w') as f:
    pg.print_table(T1=dat.T1, T2=dat.T2, T3=dat.T3, N1=dat.N1, N2=dat.N2, H=dat.H, file=f)

    if dat.T1 >= dat.T2 or dat.T2 >= dat.T3 or dat.T1 >= dat.T3:
        print('Error T1<T2<T3', file=f)
        exit()

    if dat.N1 < 0 or dat.N1 > 5:
        print('Error 0<=N1<=5', file=f)
        exit()

    if dat.N2 < 0 or dat.N2 > 5:
        print('Error 0<=N2<=5', file=f)
        exit()

    if dat.H <= 0:
        print('Error H>0', file=f)
        exit()

    xi = [x for x in range(dat.X0, dat.Xn, dat.H)]
    i = [x for x in range(0, len(xi))]
    yi = [dat.IMPL_FUNC(x) for x in xi]
    pg.print_table(i=i, xi=xi, yi=yi, file=f)

    print(file=f)
    print('LAGRANGE', file=f)

    x1 = selection(xi, dat.T1, dat.N1)
    y1 = [dat.IMPL_FUNC(elem) for elem in x1]
    lagrange1 = ip.lagrange(dat.N1, x1, y1, dat.T1)
    val1 = dat.IMPL_FUNC(dat.T1)
    print('--------------------------------------------------------------------', file=f)
    print('Ln(T1) =', lagrange1, 'nodes', x1, file=f)
    print('f(T1) =', val1, file=f)
    print('Rn(T1) =', ip.residual_term(dat.T1, x1, dat.N1, dat.MAX_DER_FUNC), file=f)
    print('|f(T1) - L' + str(dat.N1) + '(T1)| =', abs(val1-lagrange1), file=f)
    print('--------------------------------------------------------------------', file=f)

    x2 = selection(xi, dat.T2, dat.N1)
    y2 = [dat.IMPL_FUNC(elem) for elem in x2]
    lagrange2 = ip.lagrange(dat.N1, x2, y2, dat.T2)
    val2 = dat.IMPL_FUNC(dat.T2)
    print('Ln(T2) =', lagrange2, 'nodes', x2, file=f)
    print('f(T2) =', val2, file=f)
    print('Rn(T2) =', ip.residual_term(dat.T2, x2, dat.N1, dat.MAX_DER_FUNC), file=f)
    print('|f(T2) - L' + str(dat.N1) + '(T2)| =', abs(val2 - lagrange2), file=f)
    print('--------------------------------------------------------------------', file=f)

    x3 = selection(xi, dat.T3, dat.N1)
    y3 = [dat.IMPL_FUNC(elem) for elem in x3]
    lagrange3 = ip.lagrange(dat.N1, x3, y3, dat.T3)
    val3 = dat.IMPL_FUNC(dat.T3)
    print('Ln(T3) =', lagrange3, 'nodes', x3, file=f)
    print('f(T3) =', val3, file=f)
    print('Rn(T3) =', ip.residual_term(dat.T3, x3, dat.N1, dat.MAX_DER_FUNC), file=f)
    print('|f(T3) - L' + str(dat.N1) + '(T3)| =', abs(val3 - lagrange3), file=f)
    print('--------------------------------------------------------------------', file=f)

    print(file=f)
    print('NEWTON', file=f)

    x4 = selection(xi, dat.T1, dat.N2)
    y4 = [dat.IMPL_FUNC(elem) for elem in x4]
    newton1 = ip.newton(dat.N2, x4, y4, dat.T1)
    print('--------------------------------------------------------------------', file=f)
    print('Nn(T1) =', newton1, 'nodes', x4, file=f)
    print('f(T1) =', val1, file=f)
    print('Rn(T1) =', ip.residual_term(dat.T1, x4, dat.N2, dat.MAX_DER_FUNC), file=f)
    print('|f(T1) - N' + str(dat.N2) + '(T1)| =', abs(val1 - newton1), file=f)
    print('--------------------------------------------------------------------', file=f)

    x5 = selection(xi, dat.T2, dat.N2)
    y5 = [dat.IMPL_FUNC(elem) for elem in x5]
    newton2 = ip.newton(dat.N2, x5, y5, dat.T2)
    print('Nn(T2) =', newton2, 'nodes', x5, file=f)
    print('f(T2) =', val2, file=f)
    print('Rn(T2) =', ip.residual_term(dat.T2, x5, dat.N2, dat.MAX_DER_FUNC), file=f)
    print('|f(T2) - N' + str(dat.N2) + '(T2)| =', abs(val2 - newton2), file=f)
    print('--------------------------------------------------------------------', file=f)

    x6 = selection(xi, dat.T3, dat.N2)
    y6 = [dat.IMPL_FUNC(elem) for elem in x6]
    newton3 = ip.newton(dat.N2, x6, y6, dat.T3)
    print('Nn(T3) =', newton3, 'nodes', x6, file=f)
    print('f(T3) =', val3, file=f)
    print('Rn(T3) =', ip.residual_term(dat.T3, x6, dat.N2, dat.MAX_DER_FUNC), file=f)
    print('|f(T3) - N' + str(dat.N2) + '(T3)| =', abs(val3 - newton3), file=f)
    print('--------------------------------------------------------------------', file=f)

    functions = {
        "f(x)": dat.FUNC,
        "L" + str(dat.N1) + "(x) to T1": ip.lagrange(dat.N1, x1, y1, dat.X),
        "L" + str(dat.N1) + "(x) to T2": ip.lagrange(dat.N1, x2, y2, dat.X),
        "L" + str(dat.N1) + "(x) to T3": ip.lagrange(dat.N1, x3, y3, dat.X),
        "N" + str(dat.N2) + "(x) to T1": ip.newton(dat.N2, x4, y4, dat.X),
        "N" + str(dat.N2) + "(x) to T2": ip.newton(dat.N2, x5, y5, dat.X),
        "N" + str(dat.N2) + "(x) to T3": ip.newton(dat.N2, x6, y6, dat.X),
    }
    colors = {
        "f(x)": "blue",
        "L" + str(dat.N1) + "(x) to T1": "red",
        "L" + str(dat.N1) + "(x) to T2": "green",
        "L" + str(dat.N1) + "(x) to T3": "black",
        "N" + str(dat.N2) + "(x) to T1": "gray",
        "N" + str(dat.N2) + "(x) to T2": "aqua",
        "N" + str(dat.N2) + "(x) to T3": "purple",
    }
    pg.show_graph(dat.X, functions, colors)
