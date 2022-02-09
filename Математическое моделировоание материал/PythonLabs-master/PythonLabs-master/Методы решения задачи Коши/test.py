from sympy import Symbol,diff,exp,cos,sin,Matrix,var,symbols
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt

n=3
# y1,y2,y3=symbols('y[0] y[1] y[2]')
t=Symbol('t')
y = sym.Matrix(n, 1, lambda i,j:var('y[%d]' % (i+1)))

def f(T,y):
    return sym.Matrix([y[1],-y[1]+4*y[0]+T*exp(-T),2*y[2]])

A='def pfpt(t,y):\n\treturn np.array(%s)'%(str(f(t,y).diff(t)).replace('Matrix(','').replace('))',')'))+'\n'+\
	'def p2fpt2(t,y):\n\treturn np.array(%s)'%(str(f(t,y).diff(t).diff(t)).replace('Matrix(','').replace('))',')'))+'\n'+\
	'def J(t,y):\n\treturn np.array(%s)'%(str(f(t,y).jacobian(y)).replace('Matrix(','').replace('))',')'))+'\n'+\
	'def pJpt(t,y):\n\treturn np.array(%s)'%(str(f(t,y).jacobian(y).diff(t)).replace('Matrix(','').replace('))',')'))

# def Calculate(T,Y): 
#     dic={t:T}
#     [dic.update({'y'+str(i+1):Y[i]}) for i in range(n)]
#     return np.array(f(t,y).diff(t).subs(dic).evalf().T)[0],\
#             np.array(f(t,y).diff(t).diff(t).subs(dic).evalf().T)[0],\
#             np.array(f(t,y).jacobian(y).subs(dic).evalf()),\
#             np.array(f(t,y).jacobian(y).diff(t).subs(dic).evalf()),\
#             np.array(f(t,y).subs(dic).evalf().T)[0]
#  pfpt,p2fpt2,J,pJpt,F