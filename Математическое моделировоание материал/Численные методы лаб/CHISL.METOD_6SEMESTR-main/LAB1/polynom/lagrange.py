

from common.utils import formatNumber, iterate


# факториал
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# нахождение минимального индекса элемента который больше чем наш элемент
# для Xs = [1, 2, 3, 5] и x = 4
# вернет 4(5 больше 4)
def find_interval_end_index(Xs, x):
    i = 0
    while i < len(Xs):
        if Xs[i] > x:
            return i
        else:
            i += 1
    return i

# метод Лагранжа
# X = значение для которого аппроксимируем
# n = степень многочлена
# Xs = аргументы функции(из таблицы)
# Ys = значения функции(из таблицы)
def Ln(X, n, Xs, Ys):

    end_index = find_interval_end_index(Xs, X)#находим начальный индкс
    start_index = end_index - n# конечный

    if start_index < 0:# если нам нехватает элементов из таблицы, то мы просто уменьшаем промежуток по которому будет работь лагранж
        start_index = 0
        n = end_index
 
    print("используем элемент от x{start} до x{end}".format(start=start_index, end=end_index))
    formula_presentation = ""#то где будет хранить формулу в текстовом формате(для последующего построения и демонастрции Елене Антаольевне :)
    sum = 0
    for k in range(start_index, end_index + 1):#проходимся от start_index до end_index + 1
        nominator_presentation = ""
        nominator = 1#числитель
        for t in range(start_index, end_index + 1):
            if t == k:
                continue
            nominator *= (X - Xs[t])
            nominator_presentation += "( x - " + (formatNumber(Xs[t]))  + " ) * "
        nominator_presentation = "(" + nominator_presentation[0:-3] + ")"
        denominator = 1
        denominator_presentation = ""
        for t in range(start_index, end_index + 1):
            if t == k:
                continue
            denominator *= (Xs[k] - Xs[t])
            denominator_presentation += "( " + formatNumber(Xs[k]) + " - " + (formatNumber(Xs[t]))  + " ) * "
        denominator_presentation = "(" + denominator_presentation[0:-3] + ")"
        sum += nominator / denominator * Ys[k]
        formula_presentation += "(" + nominator_presentation + " / " + denominator_presentation + " * " + str(Ys[k]) + ") + "
    formula_presentation = formula_presentation[0:-3]
    print('FOMULA: {formula}'.format(formula=formula_presentation))
    return sum


# нужно найти максимум функции(https://bugaga.net.ru/ege/math/ekstremum.html#:~:text=%D0%95%D1%81%D0%BB%D0%B8%20%D0%BF%D1%80%D0%B8%20%D0%BF%D1%80%D0%BE%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%B0%D0%BA%D1%83%D1%8E,%D0%BE%D1%82%D1%80%D0%B5%D0%B7%D0%BA%D0%B0%20%D0%B8%20%D0%B2%20%D1%82%D0%BE%D1%87%D0%BA%D0%B0%D1%85%20%D1%8D%D0%BA%D1%81%D1%82%D1%80%D0%B5%D0%BC%D1%83%D0%BC%D0%B0.)
# для того чтобы доказать что функция возрастает от 1 до 2
# для этоо находим производные
# нужно найти производную функции
# в онлайн калькуляторе 3 * (x + 1)^2 + 1 / x (https://math.semestr.ru/math/diff.php)
# 1 степени  3 * (x + 1)^2 + 1 / x
# 2 степени 6x + 6 - 1/x^2
# 3 степени 6 + (2 / x ^ 3)
# 4 степень - 6 / (x ^ 4)
# 5 степень 24 / (x^5)
# 6 степеь - 120 / (x^6
# )
# нужно
M = [  # массив фукнции производных функции
    0,# 0,          # нулевая степень не нужна
    lambda x: 3 * (x + 1)**2 + 1 /x,            # максимум первой роизводной функции
    lambda x: 6 * x  +  6 - 1 / (x ** 2),                                 # максимум второй и т.д.
    lambda x: 6 + 2 / (x ** 3),
    lambda x: - 6 / (x ** 4),
    lambda x:  24 / (x**5),
    lambda x: - 120 / (x**6),
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
    # lambda x: 1,
]



def omega(Xs, x, from_index, to_index):
    result = 1
    i= from_index
    while from_index <= to_index:
        result *= x - Xs[i]
        from_index += 1
    return result


def findError(n, x, Xs):
    interval_end_index = find_interval_end_index(Xs, x)
    interval_end_value = Xs[interval_end_index]
    interval_start_index = interval_end_index - n

    return (abs(M[n + 1](interval_end_value)) # берет одну из производных в M и вычсляет значение для конца отрезка
            / factorial(n + 1)) * abs(omega(Xs, x, interval_start_index, interval_end_index))


