# начинает итерацию от start до end с шаком step вызывая на каждом шаге callback с текущим значением(просто утилитный метод)
def onRange(start, end, step, callback):
    if start < end:
        current = start
        while current <= end:
            callback(current)
            current += step

    elif end < start:
        current = start
        while current >= end:
            callback(current)
            current -= step
    else:
        callback(start)

# проход по коллекции collection вызывая при этом callback для каждого элемента
def iterate(collection, callback):
    for index in range(len(collection)):
        callback(index, collection[index])

# форматирование каждого числа, с точностью до 5 знаков после запятой
def format_number(number):
    return "{value:.5f}".format(value=number)