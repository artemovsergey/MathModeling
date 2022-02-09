from spline import calc_spline, find_interval_end_index
from common.utils import format_number
from math import log, pi as PI, sin, log

X0 = 1
XN = 2
H = 0.2
INPUT_VALUES = [X0 + 0.3, X0 + 0.5 * H, XN - 0.5 * H]

def F(x):
    return log(x) + (x + 1) ** 3

print ("===================TABLE=====================")
current = X0
print('   X   |   Y  ')
Xs = []
Ys = []
while current < XN:
    print(format_number(current), format_number(F(current)))
    Xs.append(current)
    Ys.append(F(current))
    current += H

polynoms = calc_spline(Xs, Ys)

for target in INPUT_VALUES:
    print("========РАСЧЕТ ДЛЯ ЗНАЧЕНИЯ {value}=======".format(value=target))
    x_index = find_interval_end_index(Xs, target)
    print("Выбран интервал от x{start} до x{end}".format(start=x_index - 1, end=x_index))
    interpolated_result = polynoms[x_index - 1](target)
    actual_result = F(target)
    print("Интерполир. значение: {value}".format(value=interpolated_result))
    print("Действительное значение: {value}".format(value=actual_result))
    print("Ошибка: {error}".format(error=abs(interpolated_result - actual_result)))