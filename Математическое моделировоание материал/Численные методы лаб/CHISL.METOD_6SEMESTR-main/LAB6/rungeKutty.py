from utils.format import format_number
from utils.create_array import create_array

def fillTable(start, h, n, foo, fooExact, y0):
    #Создаем двумерный массив
    data = create_array(n)

    for i in range(0, n):
        data[i] = create_array(8)

    for i in range(0, n):
        #Xi
        data[i][0] = start + i*h
        if i == 0:
            #Начальное условие
            data[i][1] = y0
            #Ki, i=1,...,4
            data[i][3] = 0
            data[i][4] = 0
            data[i][5] = 0
            data[i][6] = 0
        else:
            #Подсчет Ki, i=1,...,4
            k1 = foo(data[i-1][0], data[i-1][1])
            k2 = foo(data[i-1][0]+h/2, data[i-1][1]+h/2*k1)
            k3 = foo(data[i-1][0]+h/2, data[i-1][1]+h/2*k2)
            k4 = foo(data[i-1][0]+h, data[i-1][1]+h*k3)
            #Подсчет Yi по методу Тимона и Пумбы)))
            data[i][1] = data[i-1][1]+(1/6)*h*(k1+2*k2+2*k3+k4)
            #Записываем Ki, i=1,...,4 в таблицу
            data[i][3] = k1
            data[i][4] = k2
            data[i][5] = k3
            data[i][6] = k4
        #Точное решение
        data[i][2] = fooExact(start + h * i)
        #Погрешность
        data[i][7] = abs(data[i][1]-data[i][2])
    return data

def rungeKuttyTable(start, h, n, foo, fooExact, yo):
    data = fillTable(start, h, n, foo, fooExact, yo)

    print('=======================================Метод Рунге-Кутты==========================================')
    print('  ', 'Xi', '    ', 'Yi', '      ', 'Yточное', '     ', 'k1', '        ', 'k2', '        ', 'k3', '        ', 'k4', '    ', 'Погрешность')
    for i in range(0, n):
        print(format_number(data[i][0]), '\t', format_number(data[i][1]), '\t', format_number(data[i][2]), '\t',
            format_number(data[i][3]), '\t', format_number(data[i][4]), '\t', format_number(data[i][5]), '\t',
            format_number(data[i][6]), '\t', format_number(data[i][7]))

def fillTableSystem(start, h, n, fooF, fooG, fooExact, y0, z0):
    #Создаем двумерный массив
    data = create_array(n)

    for i in range(0, n):
        data[i] = create_array(13)

    for i in range(0, n):
        #Xi
        data[i][0] = start + i*h
        if i == 0:
            #Начальное условие
            data[i][1] = y0
            data[i][2] = z0

            #Ki, i=1,...,4
            data[i][4] = 0
            data[i][5] = 0
            data[i][6] = 0
            data[i][7] = 0

            #Li, i=1,...,4
            data[i][8] = 0
            data[i][9] = 0
            data[i][10] = 0
            data[i][11] = 0
        else:
            #Подсчет Ki,Li, i=1,...,4
            k1 = fooF(data[i-1][0], data[i-1][1], data[i-1][2])
            l1 = fooG(data[i-1][0], data[i-1][1], data[i-1][2])

            k2 = fooF(data[i-1][0]+h/2, data[i-1][1]+h/2*k1, data[i-1][2]+h/2*l1)
            l2 = fooG(data[i-1][0]+h/2, data[i-1][1]+h/2*k1, data[i-1][2]+h/2*l1)

            k3 = fooF(data[i-1][0]+h/2, data[i-1][1]+h/2*k2, data[i-1][2]+h/2*l2)
            l3 = fooG(data[i-1][0]+h/2, data[i-1][1]+h/2*k2, data[i-1][2]+h/2*l2)

            k4 = fooF(data[i-1][0]+h, data[i-1][1]+h*k3, data[i-1][2]+h*l3)
            l4 = fooG(data[i-1][0]+h, data[i-1][1]+h*k3, data[i-1][2]+h*l3)

            #Подсчет Yi и Zi по методу Тимона и Пумбы
            data[i][1] = data[i-1][1]+(1/6)*h*(k1+2*k2+2*k3+k4)
            data[i][2] = data[i-1][2]+(1/6)*h*(l1+2*l2+2*l3+l4)

            #Записываем Ki, i=1,...,4 в таблицу
            data[i][4] = k1
            data[i][5] = k2
            data[i][6] = k3
            data[i][7] = k4

            #Записываем Li, i=1,...,4 в таблицу
            data[i][8] = l1
            data[i][9] = l2
            data[i][10] = l3
            data[i][11] = l4
        #Точное решение
        data[i][3] = fooExact(start + h * i)
        #Погрешность
        data[i][12] = abs(data[i][1]-data[i][3])
    return data

def rungeKuttyTableSystem(start, h, n, fooF, fooG, fooExact, y0, z0):
    #Подсчет таблицы
    data = fillTableSystem(start, h, n, fooF, fooG, fooExact, y0, z0)

    print('=================================Система методом Рунге-Кутты======================================')
    print('  ', 'Xi', '  ', 'Yi', '   ', 'Zi', ' ', 'Точное', ' ', 'k1', '   ', 'k2', '   ', 'k3', '   ', 'k4', '   ',
        'l1', '   ', 'l2', '   ', 'l3', '   ', 'l4', ' ', 'Погрешность')
    for i in range(0, n):
        print(format_number(data[i][0]), format_number(data[i][1]), format_number(data[i][2]),
            format_number(data[i][3]), format_number(data[i][4]), format_number(data[i][5]),
            format_number(data[i][6]), format_number(data[i][7]), format_number(data[i][8]),
            format_number(data[i][9]), format_number(data[i][10]), format_number(data[i][11]),
            format_number(data[i][12]))