import data as dat
import plotgraphs as pg
import interspline as inter
import config


with open(config.FILE_NAME, 'w') as f:
    if dat.X0 >= dat.Xn:
        print('Error Xn>X0', file=f)
        exit()

    if dat.H <= 0:
        print('Error H>0', file=f)
        exit()

    print('Input data:', file=f)
    pg.print_table(X0=dat.X0, Xn=dat.Xn, H=dat.H, **dat.POINTS, file=f)
    print(file=f)

    print('Output data:', file=f)
    xi = [x for x in range(dat.X0, dat.Xn + 1, dat.H)]
    yi = [dat.FUNC(x) for x in xi]
    pg.print_table(i=[x for x in range(0, len(xi))], xi=xi, yi=yi, file=f)
    print(file=f)

    ai, bi, ci, di = inter.get_coefficients(yi, xi)
    coefficients = {'ai': ai, 'bi': bi, 'ci': ci, 'di': di}
    for key in coefficients:
        inf = 'i = 0,...,' if key == 'ci' else 'i = 1,...,'
        print('{0}: {1} {2}'.format(key, coefficients[key], inf + str(len(yi)-1)), file=f)
    print(file=f)

    x = dat.np.linspace(dat.X0, dat.Xn, 100)
    functions = {"f(x)": dat.FUNC(x)}
    arr_x = {"f(x)": x}
    colors = {"f(x)": "blue"}

    segments = list()
    for i in range(1, len(yi)):
        segments.append((xi[i-1], xi[i]))
        x = dat.np.linspace(xi[i-1], xi[i], 100)
        key = "S{i!s}(x)".format(i=i)
        arr_x[key] = x
        functions[key] = dat.INTERPOLATION_SPLINE(ai[i-1], bi[i-1], ci[i], di[i-1], xi[i], x)
        colors[key] = config.COLORS[i-1]
        print('{key} = {ai} + ({bi!s}) * (x - {xi!s}) + ({ci!s}) / 2 * (x - {xi!s})^2 + ({di!s}) / 6 * (x - '
              '{xi!s})^3, x = [{x0!s}, {xi}]'.format(key=key, i=i, ai=ai[i-1], bi=bi[i-1], xi=xi[i],
              ci=ci[i], di=di[i-1], x0=xi[i-1]), file=f)
    print(file=f)

    for key in dat.POINTS:
        for i, segment in enumerate(segments):
            if segment[0] <= dat.POINTS[key] <= segment[1]:
                print('S{i!s}({key}) = {res!s}'.format(i=i+1, key=key, res=dat.INTERPOLATION_SPLINE(
                    ai[i], bi[i], ci[i+1], di[i], segment[1], dat.POINTS[key])), file=f)
                print('f({key}) = {res!s}'.format(key=key, res=dat.FUNC(dat.POINTS[key])), file=f, end='\n\n')

pg.show_graph(arr_x, functions, colors)
