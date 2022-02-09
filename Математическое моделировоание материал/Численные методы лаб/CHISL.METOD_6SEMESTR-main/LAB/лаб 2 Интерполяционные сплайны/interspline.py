import numpy as np


def get_coefficients(yi, xi):
    ai = [yi[i] for i in range(1, len(yi))]
    hi = [xi[i] - xi[i - 1] for i in range(1, len(yi))]

    vector_b = [6 * (((yi[i+1] - yi[i]) / hi[i]) -
                     ((yi[i] - yi[i-1]) / hi[i-1])) for i in range(1, len(yi) - 1)]
    vector_b.insert(0, 0)
    vector_b.append(0)

    matrix_a = np.zeros((len(vector_b), len(vector_b)))
    matrix_a[0][0] = 1
    matrix_a[len(vector_b)-1][len(vector_b)-1] = 1
    for i in range(1, len(vector_b)-1):
        matrix_a[i][i - 1] = hi[i-1]
        matrix_a[i][i] = 2 * (hi[i-1] + hi[i])
        matrix_a[i][i+1] = hi[i]

    ci = np.linalg.solve(matrix_a, vector_b)
    di = [(ci[i] - ci[i-1]) / hi[i-1] for i in range(1, len(yi))]

    return ai, [(ci[i] * hi[i-1] / 2) - (di[i-1] * pow(hi[i-1], 2) / 6) +
                ((yi[i] - yi[i-1]) / hi[i-1]) for i in range(1, len(yi))], ci, di
