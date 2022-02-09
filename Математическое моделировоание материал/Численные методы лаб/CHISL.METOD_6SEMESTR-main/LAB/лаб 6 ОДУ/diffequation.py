def euler_method(func, h, xi, y0):
    yi = [y0]
    for i in range(0, len(xi) - 1):
        yi.append(yi[i] + h * func(xi[i], yi[i]))
    return yi


def midpoint_method(func, h, xi, y0):
    const, yi = h / 2, [y0]
    for i in range(0, len(xi) - 1):
        yi.append(yi[i] + h * func(xi[i] + const, yi[i] + const * func(xi[i], yi[i])))
    return yi


def trapezoid_method(func, h, xi, y0):
    const, yi = h / 2, [y0]
    for i in range(0, len(xi) - 1):
        yi.append(yi[i] + const * (func(xi[i], yi[i]) + func(xi[i + 1], yi[i] + h * func(xi[i], yi[i]))))
    return yi


def runge_kutta_method(func, h, xi, y0):
    const, yi = h / 2, [y0]
    for i in range(0, len(xi) - 1):
        k1 = func(xi[i], yi[i])
        k2 = func(xi[i] + const, yi[i] + const * k1)
        k3 = func(xi[i] + const, yi[i] + const * k2)
        k4 = func(xi[i] + h, yi[i] + h * k3)
        yi.append(yi[i] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4))
    return yi


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
