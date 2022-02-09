from common.utils import on_range, summarize_range

def find_antiderivative_with_middle_rectangles(f, x0, h, n):
    return summarize_range(0, n - 1, 1, lambda i: f(x0 + (i + 0.5) * h) * h)

def find_antiderivative_with_left_rectangles(f, x0, h, n):
    return summarize_range(1, n, 1, lambda i: f(x0 + (i - 1) * h) * h)

def find_antiderivative_with_right_rectangles(f, x0, h, n):
    return summarize_range(1, n, 1, lambda i: f(x0 + i * h) * h)

def find_antiderivative_with_trapezoid(f, x0, h, n):
    return summarize_range(1, n, 1, lambda i: ((f(x0 + i * h) + f(x0 + (i - 1) * h)) / 2) * h)

# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5_%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5#%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BF%D0%B0%D1%80%D0%B0%D0%B1%D0%BE%D0%BB_(%D0%BC%D0%B5%D1%82%D0%BE%D0%B4_%D0%A1%D0%B8%D0%BC%D0%BF%D1%81%D0%BE%D0%BD%D0%B0)
def find_antiderivative_with_parabola(f, x0, h, n):
    a = x0
    b = x0 + h * n
    def simpsonFunc(f, a, b, N, i):
        return f(a + (((b - a) * i)/(2 * N)))

    first_factor = (b - a) / (6 * n)
    odd_sum = summarize_range(1, 2 * n - 1, 2, lambda i: simpsonFunc(f, a, b, n, i))
    even_sum = summarize_range(2, 2 * n - 2, 2, lambda i: simpsonFunc(f, a, b, n, i))
    return first_factor * (simpsonFunc(f, a, b, n, 0) + 4 * odd_sum + 2 * even_sum + simpsonFunc(f, a, b, n, 2 * n))

# https://www.wikiwand.com/ru/%D0%A7%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5_%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5#/google_vignette
X = [0.93246951, -0.93246951, 0.66120939, -0.66120939, 0.23861919, -0.23861919]
C = [0.17132449, 0.17132449, 0.36076157, 0.36076157, 0.46791393, 0.46791393]

def find_antiderivative_with_gauss(f, x0, h, n):
    global X
    global C
    a = x0
    b = x0 + h * n

    return ((b - a) / 2) * (summarize_range(0, n - 1, 1, lambda i: C[i] * f(((b - a) / 2) * X[i] + (b + a) / 2)))