from sympy import Symbol,diff,exp,cos,sin,Matrix,var,symbols
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt

n=3
y1,y2,y3=symbols('y1 y2 y3')
t=Symbol('t')
y = Matrix(n, 1, lambda i,j:var('y%d' % (i+1)))

def f(T,y):
    return Matrix([y[1],-y[1]+4*y[0]+T*exp(-T),2*y[2]])

def Calculate(T,Y): 
    dic={t:T}
    [dic.update({'y'+str(i+1):Y[i]}) for i in range(n)]
    return np.array(f(t,y).diff(t).subs(dic).evalf().T)[0],\
            np.array(f(t,y).diff(t).diff(t).subs(dic).evalf().T)[0],\
            np.array(f(t,y).jacobian(y).subs(dic).evalf()),\
            np.array(f(t,y).jacobian(y).diff(t).subs(dic).evalf()),\
            np.array(f(t,y).subs(dic).evalf().T)[0]



yn=np.array([1,0,1])
Tn,tmax=0,2
h=0.01

Time=np.array([])
Y1=np.array([])
Y2=np.array([])
Y3=np.array([])
while Tn<=tmax:
    print(Tn)
    Tn=Tn+h
    yo=yn
    Time=np.append(Time,Tn)
    Y1=np.append(Y1,yo[0])
    Y2=np.append(Y2,yo[1])
    Y3=np.append(Y3,yo[2])
    pfpt,p2fpt2,J,pJpt,F=Calculate(Tn,yn)
    yn=np.array(yn+h*(F+h/2*(pfpt+np.dot(J,F))+h**2/6*(p2fpt2+np.dot(pJpt,F)+np.dot(J,pfpt))))
plt.subplot(221)
plt.plot(Time,Y1)
# plt.show()
plt.subplot(222)
plt.plot(Time,Y2)
# plt.show()
plt.subplot(223)
plt.plot(Y1,Y2)
plt.subplot(224)
plt.plot(Time,Y3,'*r',Time,np.exp(2*np.array(Time)),'-b')
plt.show()