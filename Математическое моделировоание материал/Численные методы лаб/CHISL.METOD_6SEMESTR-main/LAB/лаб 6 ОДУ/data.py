import math

INTERVAL = [0, 0.3]  # [0, 1]
H = 0.05  # 0.1
F0 = 2  # 1
FUNC_EXACT = lambda x: 2 / math.sqrt(1 + x ** 2)  # 0.75 * math.e ** (-2 * x) + 0.5 * x ** 2 - 0.5 * x + 0.25
FUNC = lambda x, y: (-x * y) / (1 + x ** 2)  # x ** 2 - 2 * y
ACCURACY = 2  # 1
# ---------------------------------------------------------------------------------
INTERVAL1 = [0, 1]
H1 = 0.2
Y0 = 1
Z0 = 3
FUNC1 = lambda x, y, z: z
FUNC2 = lambda x, y, z: (2 * x * z) / (x ** 2 + 1)
FUNC_EXACT1 = lambda x: x ** 3 + 3 * x + 1
ACCURACY1 = 1
