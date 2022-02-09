
from polynom.newton import newton


Ys = [
    1.5,
    1,
    3
]

Xs = [-1, 0, 1]

result, presentation = newton(Ys, Xs, 2, 0.5)
print(result, presentation)