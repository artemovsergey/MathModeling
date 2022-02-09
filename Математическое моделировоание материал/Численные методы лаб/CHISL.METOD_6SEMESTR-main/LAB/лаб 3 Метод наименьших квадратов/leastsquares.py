from sympy import *


def get_function(func, xi, yi, x, *parameters):
    partial_der = [diff(func, elem) for elem in parameters]  # Частные производные func

    system_equations = list()  # Система уравнений
    for der in partial_der:
        equation = 0
        for i, val in enumerate(xi):
            equation += (func.subs({x: val}) - yi[i]) * der.subs({x: val})
        system_equations.append(equation)

    return func.subs(solve(system_equations, parameters))


def dev_rate(func, xi, yi, x):  # Норма отклонения
    dev = 0
    for i, val in enumerate(xi):
        dev += (func.subs({x: val}) - yi[i]) ** 2
    return dev
