from common.utils import onRange

def generate_array(size, default=None):
    return [default for i in range(size)]

def find_interval_end_index(Xs, x):
    i = 0
    while i < len(Xs):
        if Xs[i] > x:
            return i
        else:
            i += 1
    return i

def calc_spline(Xs, Ys):
    N = len(Ys) - 1
    As = generate_array(N + 1)
    def callback(i):
        As[i] = Ys[i]
    onRange(1, N, 1, callback)

    Hs = generate_array(N + 1)
    for i in range(1, N + 1):
        Hs[i] = Xs[i] - Xs[i - 1];

    Ls = generate_array(N + 1)

    for i in range(1, N + 1):
        Ls[i] = (Ys[i] - Ys[i - 1])/Hs[i]

    Deltas = generate_array(N + 1)
    Lambdas = generate_array(N + 1)

    Deltas[1] = - Hs[2] / (2 * (Hs[1] + Hs[2]))
    Lambdas[1] = 3 * (Ls[2] - Ls[1]) / (2 * (Hs[1] + Hs[2]))
    
    for k in range(3, N + 1):
        Deltas[k - 1] = - Hs[k] / (2 * Hs[k - 1] + 2 * Hs[k] + Hs[k - 1] * Deltas[k - 2])

    for k in range(3, N + 1):
        Lambdas[k - 1] = (3 * Ls[k] - 3 * Ls[k - 1] - Hs[k - 1] * Lambdas[k - 2]) / ( 2 * Hs[k - 1] + 2 * Hs[k] + Hs[k - 1] * Deltas[k - 2])

    Cs = generate_array(N + 1, 0)
    Cs[0] = 0

    def callback(k):
        Cs[k - 1] = Deltas[k - 1] * Cs[k] + Lambdas[k - 1]
    onRange(N, 2, 1, callback)

    Bs = generate_array(N + 1)
    def callback(k):
        Bs[k] = Ls[k] + (2 * Cs[k] * Hs[k] + Hs[k] * Cs[k - 1]) / 3
    onRange(1, N, 1, callback)

    Ds = generate_array(N + 1)
    def callback(k):
        Ds[k] = (Cs[k] - Cs[k - 1]) / (3 * Hs[k])
    onRange(1, N, 1, callback)

    polynoms = []
    def callback(N):
        print('На интервале от {start} до {end}'.format(start=str(Xs[N - 1]), end=str(Xs[N])))
        print('{ak} + {bk} * (x - {xk}) + {ck} * (x - {xk}) ^ 2 + {dk} * (x - {xk}) ^ 3'.format(ak=As[N], bk=Bs[N], xk=Xs[N], ck=Cs[N], dk=Ds[N]))
        # polynoms это массив из функций полиномов
        polynoms.append(lambda x: As[N] + Bs[N] * (x - Xs[N]) + Cs[N] * (x - Xs[N]) ** 2 + Ds[N] * (x - Xs[N]) ** 3)

    onRange(1, N, 1, callback)
    return polynoms