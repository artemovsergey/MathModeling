import numpy as np

X0 = 1  # начало отрезка
Xn = 11  # конец отрезка
H = 2  # шаг
T1 = X0 + 0.3
T2 = X0 + 0.5 * H
T3 = Xn - 0.5 * H

POINTS = {
    'T1': T1,
    'T2': T2,
    'T3': T3,
}

FUNC = lambda x: 5 * x - 8 * np.log(x) - 8  # реализация f(x)
INTERPOLATION_SPLINE = lambda ai, bi, ci, di, xi, x: ai + bi * (x - xi) + ci / 2 * (x - xi) ** 2 + di / 6 * (
            x - xi) ** 3  # реализация Si(x)
