from sympy import symbols, log

FILE_NAME = 'output-data.txt'

a, b, c, d, x = symbols('a, b, c, d, x')

FUNC_1 = a * x + b
FUNC_2 = a * x ** 2 + b * x + c
FUNC_3 = a * x ** 3 + b * x ** 2 + c * x + d
