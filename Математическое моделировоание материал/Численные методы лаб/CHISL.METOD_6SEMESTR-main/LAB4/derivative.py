# f функция
# X массив точек x

def find_right_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

def find_left_derivative(f, x, h):
    return (f(x) - f(x - h)) / h

def find_center_derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def find_second_power_derivative(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h ** 2