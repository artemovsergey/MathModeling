from derivative import find_center_derivative, find_left_derivative, find_right_derivative, find_second_power_derivative
from common.utils import on_range
from math import exp

"""
H = 0.2
X0 = 0
XN = 1
f1 = lambda x: x ** 3
# первая производная 
f1d = lambda x: 3 * x ** 2
# вторая производная
f2d = lambda x: 6 * x
"""

H = 0.5
X0 = 3
XN = 5
f1 = lambda x: x/(x+1)**2
# первая производная 
f1d = lambda x: (-x+1)/(x+1)**3
# вторая производная
f2d = lambda x: (2*x-4)/(x+1)**4

def build_table(f, h, x1, x2):
    X = []
    Y = []
    def callback(x):
        X.append(x)
        Y.append(f(x))
    on_range(x1, x2, h, callback)
    return X, Y

def print_table(X, Y):
    print('      X    |     Y    | Y\'(точное)|  Y\'(лев)  | Y\'(прав)  | Y\'(центр) | Y\'\'(точная)| Y\'\'(приближ)')
    def callback(i):
        result = ""
        result += " {x:.6f} ".format(x=X[i])
        result += "| {y:.6f} ".format(y=Y[i])
        result += "| {yda: .6f} ".format(yda=f1d(X[i]))
        if i != 0:
            result += "| {yld: .6f} ".format(yld=find_left_derivative(f1, X[i], H))
        else:
            result += "|     ###   "
        if i != len(X) - 1:
            result += "| {yrd: .6f} ".format(yrd=find_right_derivative(f1, X[i], H))
        else:
            result += "|     ###   "
        if i != len(X) - 1 and i != 0:
            result += "| {ycd: .6f} ".format(ycd=find_center_derivative(f1, X[i], H))
        else:
            result += "|   ###     "
        result += "| {yd2pa:.6f}   ".format(yd2pa=f2d(X[i]))
        if i != len(X) - 1 and i != 0:
            result += "| {yd2pi:.6f} ".format(yd2pi=find_second_power_derivative(f1, X[i], H))
        else:
            result += "|   ### "
        print(result)
    on_range(0, len(X) - 1, 1, callback)

X, Y = build_table(f1, H, X0, XN)
print_table(X, Y)