from utils.format import format_number
from utils.create_array import create_array
def fillTable(start, h, n, foo, fooExact, y0):
    #Создаем двумерный массив
    data = create_array(n)

    for i in range(0, n):
        data[i] = create_array(4)

    for i in range(0, n):
        #Xi
        data[i][0] = start + i*h
        if(i == 0):
            #Начальное условие
            data[i][1] = y0
        else:
            #Подсчет Yi по методу средней точки
            data[i][1] = data[i-1][1]+h*foo(data[i-1][0]+h/2, data[i-1][1]+h/2*foo(data[i-1][0], data[i-1][1]))
        #Точное решение
        data[i][2] = fooExact(start + h * i)
        #Погрешность
        data[i][3] = abs(data[i][1]-data[i][2])
    return data

def midPointTable(start, h, n, foo, fooExact, yo):
    #Подсчет таблицы
    data = fillTable(start, h, n, foo, fooExact, yo)

    print('===========Метод средней точки=============')
    print('  ', 'Xi', '    ', 'Yi', '      ', 'Yточное', '  ', 'Погрешность')
    for i in range(0, n):
        print(format_number(data[i][0]), '\t', format_number(data[i][1]), '\t', format_number(data[i][2]), '\t', format_number(data[i][3]))