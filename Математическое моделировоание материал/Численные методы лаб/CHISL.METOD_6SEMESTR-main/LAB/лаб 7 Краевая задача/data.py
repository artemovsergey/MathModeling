INTERVAL = [0, 1]  # [0.5, 1]  # [0, 0.5]
H = 0.1

A1 = 1  # 0  # 1
A2 = 1  # 1  # 1
B1 = 0  # 1  # 0
B2 = 0  # 0  # 0
G1 = -0.5  # 1  # 0
G2 = -1  # 3  # 1

ACCURACY = 1

FUNC_DER_Y012 = lambda x, y, s: s
FUNC_DER_S0 = lambda x, y, s: 1 - (2 / (x - 2)) * s - (x - 2) * y  # -2 * (x ** 2) + 2 * y - (1 / x) * s
FUNC_DER_S12 = lambda x, y, s: - (2 / (x - 2)) * s - (x - 2) * y  # 2 * y - (1 / x) * s

FUNC_G = lambda x: x - 2  # -1 / x
FUNC_F = lambda x: 1  # 2 * x + 4
FUNC_P = lambda x: 2 / (x - 2)  # 1

FUNC_EXACT = lambda x: 1 / (x - 2)  # (x ** 2) + 2
