from sympy import Symbol,diff,exp,cos,sin,Matrix,var,symbols
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint,solve_ivp

# n=3
n=2
t=Symbol('t')
y = sym.Matrix(n, 1, lambda i,j:var('y[%d]' % (i)))

def f(T,y):
    return Matrix([\
                y[0],\
                -y[0]+4*y[1]+T*exp(-T),\
                # 2*y[2]\
                ])
print(np.array(f(t,y)).T[0])
A='def pfpt(t,y):\n\treturn np.array(%s)'%(str(np.array2string(np.array(f(t,y).diff(t)).T[0],separator=', ')).replace('Matrix(',''))+'\n'+\
    'def p2fpt2(t,y):\n\treturn np.array(%s)'%(str(np.array2string(np.array(f(t,y).diff(t).diff(t)).T[0],separator=', ')).replace('Matrix(',''))+'\n'+\
    'def J(t,y):\n\treturn np.array(%s)'%(str(f(t,y).jacobian(y)).replace('Matrix(',''))+'\n'+\
    'def model(t,y):\n\treturn np.array(%s)'%(str(np.array2string(np.array(f(t,y)).T[0],separator=', ')).replace('Matrix(',''))+'\n'+\
    'def pJpt(t,y):\n\treturn np.array(%s)'%(str(f(t,y).jacobian(y).diff(t)).replace('Matrix(',''))

exec(A.replace('))',')',100))

# y00=np.array([1,0,1])
y00=np.array([1,0])
Tn0,tmax0=0,2
h=0.5

Time=np.array([])
Y = np.empty((0,n),np.float32)
from numpy.linalg import norm

h=0.5
eps=0.01
N=0
while True:
    print('итерация',N)
    h=h/2

    yn=y00
    Tn=Tn0
    tmax=tmax0  

    N+=1

    OldTime=Time
    OldY=Y

    Time=np.array([])
    Y = np.empty((0,n),np.float32)

    while Tn<=tmax:

        Tn=Tn+h
        yo=yn
        Time=np.append(Time,Tn)

        Y=np.append(Y,[yo],axis=0)

        const_pfpt=pfpt(Tn,yn)
        const_J=J(Tn,yn)
        const_F=model(Tn,yn)
        yn=np.array(yn+h*(const_F+h/2*(const_pfpt+np.dot(const_J,const_F))+h**2/6*(p2fpt2(Tn,yn)+\
            np.dot(pJpt(Tn,yn),const_F)+np.dot(const_J,const_pfpt))))
    print('расчет окончен',len(Y))
    if N>=3:
        YY=Y
        YO=OldY
        if len(YY)%2!=0:
            YY=YY[:-1]
        if len(YO)%2!=0:
            YO=YO[:-1]
        YY=np.array(YY,dtype=np.float32)
        YO=np.array(YO,dtype=np.float32)
        delta=np.mean(norm(YY[0::2]-YO,axis=0))
        print(delta)
        if N>10*2:
            break
        if delta<eps:
            break

solve = solve_ivp(model,[Tn0,tmax0],y00,method='LSODA')#,min_step=0.01,max_step=0.01

Time2=np.array(solve.t)
Z=solve.y

Z1,Z2=Z
Y1,Y2=Y.T

from numpy import sqrt,exp

# def y1(t):
    # return  -1/544*exp(-1/2*(3 + sqrt(17))*t)*(34*exp(1/2*(1 + sqrt(17))*t)*(4*t - 1) + 5*(5*sqrt(17) - 51)*exp(t) - 5*(51 + 5*sqrt(17))*exp(sqrt(17)*t + t))
    # return -0.00183824*exp(-3.56155*t)*(34*exp(2.56155*t)*(4*t - 1) - 151.922*exp(t) - 358.078*exp(5.12311*t))

# def y2(T):
    # return b1*c1*np.exp(b1*T)+b2*c2*np.exp(b2*T)+1/4*np.exp(-T)*T-np.exp(-T)/8

plt.subplot(131)
plt.plot(Time,Y1)
plt.plot(Time2,Z1)
# plt.plot(Time2,y1(Time2),'r-')
plt.subplot(132)
plt.plot(Time,Y2)
plt.plot(Time2,Z2)
# plt.plot(Time2,y1(Time2),'r-')
plt.subplot(133)
plt.plot(Z1,Z2)
plt.plot(Y1,Y2)
plt.show()