from polynom.newton import newton
from common.utils import formatNumber
from math import log, pi as PI, sin, log10
from polynom.lagrange import Ln, findError, omega;
# https://bugaga.net.ru/ege/math/ekstremum.html

# я 16 в общем списке
# я 8 в списке подгруппы
# последняя цифра студенческого (зачётки) 5

INPUT_VALUES = [1.19, 3.41]
X0 = 0
XN = 5
H = 1

n1  = 2
n2 = 4

def F(x):
    return 2*x+3*log(x+0.5)
    # return sin(x)

print ("===================TABLE=====================")
# Xs = [0, 0.2, 0.4, 0.6, 0.8, 1]
# Ys = [0, 0.1987, 0.3894, 0.5646, 0.7174, 0.8415]


current = X0
print('   X   |  Y  ')
Xs = []
Ys = []
while current < XN:
    print(formatNumber(current), formatNumber(F(current)))
    Xs.append(current)
    Ys.append(F(current))
    current += H

N = n1
print ("===================LAGRANZ {N} POWER=====================".format(N=N))
for INPUT_VALUE in INPUT_VALUES:
    print("===========расчет для {value}============".format(value=INPUT_VALUE))
    result = Ln(INPUT_VALUE, N, Xs, Ys)
    actualResult = F(INPUT_VALUE)
    print("апроксимированный результат: {result}".format(result=result))
    print("реальный резльутат: {result}".format(result=actualResult))
    print("реальная ошибка: {result}".format(result = abs(actualResult - result)))
    print("аппроксимированная ошибка: {result}".format(result=findError(N, INPUT_VALUE, Xs)))
N = n2
print ("===================LAGRANZ {N} POWER=====================".format(N=N))
for INPUT_VALUE in INPUT_VALUES:
    print("===========расчет для {value}============".format(value=INPUT_VALUE))
    result = Ln(INPUT_VALUE, N, Xs, Ys)
    actualResult = F(INPUT_VALUE)
    print("апроксимированный результат: {result}".format(result=result))
    print("реальный резльутат: {result}".format(result=actualResult))
    print("реальная ошибка: {result}".format(result = abs(actualResult - result)))
    print("аппроксимированная ошибка: {result}".format(result=findError(N, INPUT_VALUE, Xs)))





print("##################################################NEWTON CALCULATIONS ###########################################")

N = n1
print ("===================NEWTON {N} POWER=====================".format(N=N))
for INPUT_VALUE in INPUT_VALUES:
    print("===========расчет для {value}============".format(value=INPUT_VALUE))
    result, presentation = newton(Ys, Xs, N, INPUT_VALUE)
    actualResult = F(INPUT_VALUE)
    print("апроксимированный результат: {result}".format(result=result))
    print("реальный резльутат: {result}".format(result=actualResult))
    print("реальная ошибка: {result}".format(result = abs(actualResult - result)))
    print("аппроксимированная ошибка: {result}".format(result=findError(N, INPUT_VALUE, Xs)))
    print("Формула: " + presentation)
N = n2
print ("===================NEWTON {N} POWER=====================".format(N=N))
for INPUT_VALUE in INPUT_VALUES:
    print("===========расчет для {value}============".format(value=INPUT_VALUE))
    result, presentation = newton(Ys, Xs, N, INPUT_VALUE)
    actualResult = F(INPUT_VALUE)
    print("апроксимированный результат: {result}".format(result=result))
    print("реальный резльутат: {result}".format(result=actualResult))
    print("реальная ошибка: {result}".format(result = abs(actualResult - result)))
    print("аппроксимированная ошибка: {result}".format(result=findError(N, INPUT_VALUE, Xs)))
    print("Формула: " + presentation)




# INPUT_VALUE = 1.55
# N = 2
# print("############DEBUG###########")
# result, presentation = newton(Ys, Xs, N, INPUT_VALUE)
# actualResult = F(INPUT_VALUE)
# print("апроксимированный результат: {result}".format(result=result))
# print("реальный резльутат: {result}".format(result=actualResult))
# print("реальная ошибка: {result}".format(result = abs(actualResult - result)))
# print("аппроксимированная ошибка: {result}".format(result=findError(N, INPUT_VALUE, Xs)))
