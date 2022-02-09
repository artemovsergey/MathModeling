from math import exp, log, cos, sin
#Функция для Задания 1 Пример 1
def task1(x, y):
    return pow(x, 2)-2*y

#Точная функция для Задания 1 Пример 1
def task1Exact(x):
    return 0.75 * exp(-2*x)+0.5 * pow(x, 2)-0.5*x+0.25

#Функция f для Задания 1 Пример 2
def task2f(x, y, z):
    return z

#Функция g для Задания 1 Пример 2
def task2g(x, y, z):
    return (2*x*z)/(pow(x, 2)+1)

#Точная функция для Задания 1 Пример 2
def task2Exact(x):
    return pow(x, 3)+3*x+1

#Функция для задания по вариантам
def task3(x, y):
    return y*cos(x) + cos(x)*sin(x)

#Точная функция для задания по вариантам
def task3Exact(x):
    return exp(-sin(x)) + sin(x) - 1