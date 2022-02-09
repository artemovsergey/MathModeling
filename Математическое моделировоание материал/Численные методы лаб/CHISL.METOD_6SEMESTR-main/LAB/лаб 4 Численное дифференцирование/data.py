import math

X0 = 0
Xn = 1
NUM_DECIMAL_PLACES = 1
H = 0.2

FUNC = lambda x: math.sin(2 * x) + 3 * x
FIRST_DER = lambda x: 2 * math.cos(2 * x) + 3
SECOND_DER = lambda x: -4 * math.sin(2 * x)
