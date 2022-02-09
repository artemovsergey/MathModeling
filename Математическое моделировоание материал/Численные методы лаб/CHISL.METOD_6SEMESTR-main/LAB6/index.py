from functions import task1, task1Exact, task2Exact, task2f, task2g, task3, task3Exact
from euler import eulerTable
from midPoint import midPointTable
from trapezoids import trapezoidsTable
from rungeKutty import rungeKuttyTable, rungeKuttyTableSystem

#Задание 1 Пример 1
start = 0
end = 1
h = 0.1
y0 = 1

n = round((end-start)/h)+1

eulerTable(start, h, n, task1, task1Exact, y0)
midPointTable(start, h, n, task1, task1Exact, y0)
trapezoidsTable(start, h, n, task1, task1Exact, y0)
rungeKuttyTable(start, h, n, task1, task1Exact, y0)

#Задание 1 Пример 2
start = 0
end = 1
h = 0.2
y0 = 1
z0 = 3

n = round((end-start)/h)+1

rungeKuttyTableSystem(start, h, n, task2f, task2g, task2Exact, y0, z0)

#Задание 2
start = 0
end = 0.5
h = 0.1
y0 = -1

n = round((end - start) / h) + 1

eulerTable(start, h, n, task3, task3Exact, y0)
midPointTable(start, h, n, task3, task3Exact, y0)
trapezoidsTable(start, h, n, task3, task3Exact, y0)
rungeKuttyTable(start, h, n, task3, task3Exact, y0)