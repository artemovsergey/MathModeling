from sympy import Symbol,diff,exp,cos,sin

x,y=Symbol('x[0]'),Symbol('x[1]')
# x,y=Symbol('{0}'),Symbol('{1}')
t=Symbol('exp(9/2)')
#t=exp(9/2)
f=(x+y**2-12*y+45)*exp(x/2)*t

#f=cos(x)*sin(y)

# f
# print(f)

# grad
# print([diff(f,x), diff(f,y)])
from sympy.matrices import *
# gessian
invH=Matrix(([diff(f,x,x),diff(f,x,y)],[diff(f,y,x),diff(f,y,y)])).inv()

Grad=Matrix([diff(f,x),diff(f,y)])
print([[diff(f,x,x),diff(f,x,y)],[diff(f,y,x),diff(f,y,y)]])
print('-')
print([diff(f,x),diff(f,y)])
# print(M.inv())
# print(Grad)

# -pk
# print(invH*Grad)