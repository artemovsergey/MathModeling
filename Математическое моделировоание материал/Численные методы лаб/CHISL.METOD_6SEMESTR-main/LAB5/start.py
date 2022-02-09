from task.antiderivative_calculations import find_antiderivative_with_gauss, find_antiderivative_with_left_rectangles, find_antiderivative_with_middle_rectangles, find_antiderivative_with_parabola, find_antiderivative_with_right_rectangles, find_antiderivative_with_trapezoid
from common.utils import summarize_range
from math import pi, exp, sin, cos

X0 = 4
XN = 6
N = 5
#H = (XN - X0) / N
H = 0.4

f = lambda x: x**2/(x-1)
#f = lambda x: exp(2 * x) * sin(x)
fad = lambda x: (x**2-2*x)/(x-1)*2

print("Точное значение: ", fad(XN) - fad(X0))
print("Метод прямоугольника(левый): ", find_antiderivative_with_left_rectangles(f, X0, H, N))
print("Метод прямоугольника(средний): ", find_antiderivative_with_middle_rectangles(f, X0, H, N))
print("Метод прямоугольника(правый): ", find_antiderivative_with_right_rectangles(f, X0, H, N))
print("Метод трапеции: ", find_antiderivative_with_trapezoid(f, X0, H, N))
print("Метод параболы: ", find_antiderivative_with_parabola(f, X0, H, N))
print("Метод Гаусса: ", find_antiderivative_with_gauss(f, X0, (XN - X0) / 6, 6))