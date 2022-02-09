from utils.format import format_number
from utils.create_array import create_array

def fillTable(start, h, n, foo, fooExact, y0):
    #Создаем двумерный массив
    data = create_array(n)

    for i in range(0, n):
        data[i] = create_array(n)

    for i in range(0, n):
        #Xi
        data[i][0] = start + i*h
        if i == 0:
            #Начальное условие
            data[i][1] = y0
        else:
            #Подсчет Yi по методу Эйлера
            data[i][1] = data[i-1][1]+h*foo(start+(i-1)*h, data[i-1][1])
        #Точное решение
        data[i][2] = fooExact(start + h * i)
        #Погрешность
        data[i][3] = abs(data[i][1]-data[i][2])
    return data

def eulerTable(start, h, n, foo, fooExact, yo):
    #Подсчет таблицы
    data = fillTable(start, h, n, foo, fooExact, yo)

    print('==============Метод Эйлера=================')
    print('  ', 'Xi', '    ', 'Yi', '      ', 'Yточное', '  ', 'Погрешность')
    for i in range(0, n):
        print(format_number(data[i][0]), '\t', format_number(data[i][1]), '\t', format_number(data[i][2]), '\t', format_number(data[i][3]))