from sympy import *
x,y = symbols("x y")
f = symbols("f")

f=cos(x)*sin(y)
f= x*y +50/x + 20/y

print(diff(f, x))
print(diff(f, y))
print(diff(diff(f, x),x))
print(diff(diff(f, x),y))
print(diff(diff(f, y),y))
# diff(f, x).subs(f, 3*x + 2) # == Derivative(3*x + 2, x) <- Why not 3?