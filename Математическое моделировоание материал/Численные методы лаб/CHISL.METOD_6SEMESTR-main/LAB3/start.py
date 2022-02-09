# x - переменная/одна функция
# X - массив переменных/массив фукнций

from common.math_utils import calc_determinant, solve_equation_system
from common.utils import iterate, onRange, summarize
from math import log

X = [-3, -2, -1, 0, 1, 2]
Y = [-1.4, -4.3, -5.2, -4.1, -1.1, 4.2]

f1 = lambda a, b: lambda x: a * x + b

def find_liniar_parameters(X, Y):
    x_in_2_param = summarize(X, lambda _, x: x ** 2)
    x_param = summarize(X, lambda _, x: x)
    n = len(X)
    y_param = summarize(Y, lambda _, y: y)
    xy_param = summarize(X, lambda i, _: X[i] * Y[i])

    solutions = solve_equation_system([
        [x_in_2_param, x_param, xy_param],
        [x_param, n, y_param]
    ])

    print('ЛИНЕЙНАЯ ФУНКЦИЯ ФОРМУЛА: {a} * x + {b}'.format(a=solutions[0], b=solutions[1]))
    func = lambda x: solutions[0] * x + solutions[1]
    return func

def find_square_parameters(X, Y):
    x_in_4_param = summarize(X, lambda _, x: x ** 4)
    x_in_3_param = summarize(X, lambda _, x: x ** 3)
    x_in_2_param = summarize(X, lambda _, x: x ** 2)
    y_and_x_in_2_param = summarize(X, lambda i, _: Y[i] * (X[i] ** 2))
    x_param = summarize(X, lambda _, x: x)
    xy_param = summarize(X, lambda i, _: X[i] * Y[i])
    y_param = summarize(Y, lambda _, y: y)
    n = len(X)

    solutions = solve_equation_system([
        [x_in_4_param, x_in_3_param, x_in_2_param, y_and_x_in_2_param],
        [x_in_3_param, x_in_2_param, x_param, xy_param],
        [x_in_2_param, x_param, n, y_param]
    ])

    print('КВАДРАТИЧНАЯ ФУНКЦИЯ ФОРМУЛА: {a} * (x ^ 2) + {b} * x + {c}'.format(a=solutions[0], b=solutions[1], c=solutions[2]))
    return lambda x: solutions[0] * (x ** 2) + solutions[1] * x + solutions[2]

# взяла фукнцию a*(1/x) + b
# производная по а равна 1/x
# по b равна 1
# система из двух уровнений
# сумма(- yi + a*(1/x) - b) * (1 / x) = 0
# сумма(- yi + a*(1 / x) - b) * 1 = 0
# после преобразования

#1) a*сум(1 / x^2) + b * сум(1 / x) = сум(yi * 1 / x)
#2) a * (1 / x) + nb = yi

def find_hyperbolic(X, Y):
    # 0 недопустим для фукнции, так что пропускаем
    X = X[0:3] + X[4:]
    Y = Y[0:3] + Y[4:]
    
    ln_in_2_x_param = summarize(X, lambda _, x: (1 / x) ** 2)
    ln_x_param = summarize(X, lambda _, x: 1 / x)
    y_lnx_param = summarize(X, lambda i, _: Y[i] * (1 / X[i]))
    n = len(X)
    y_param = summarize(Y, lambda _, y: y)

    solutions = solve_equation_system([
        [ln_in_2_x_param, ln_x_param, y_lnx_param],
        [ln_x_param, n, y_param],
    ])
    print('ГИПЕРБОЛИЧЕСКАЯ ФУНКЦИЯ ФОРМУЛА: {a} * ( 1 / x ) + {b}'.format(a=solutions[0], b=solutions[1]))
    return lambda x: solutions[0] * (1 / x) + solutions[1] if x != 0 else 0;

approximated_functions = [
    find_liniar_parameters(X, Y),
    find_square_parameters(X, Y),
    find_hyperbolic(X, Y)]
q = 0
for i in range(len(approximated_functions)):
    squred_epsilon = summarize(X, lambda t, _: (Y[t] - approximated_functions[i](X[t])) ** 2)
    q += squred_epsilon
    print("epsilon^2 для {i} функции: {error}".format(i=i + 1, error=squred_epsilon))

#print('r: ' + str(q))