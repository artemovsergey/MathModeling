from sympy import Symbol,diff,exp,cos,sin,Matrix,var,symbols
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint,solve_ivp

# n=3
n=2
y00=np.array([1,0])
Tn0,tmax0=0,2
h=0.5
eps=0.03


t=Symbol('t')
y = sym.Matrix(n, 1, lambda i,j:var('y[%d]' % (i)))

def f(T,y):
    return Matrix([\
                y[1],\
                -y[1]+4*y[0]+T*exp(-T),\
                ])

A='def pfpt(t,y):\n\treturn np.array(%s)'%(str(np.array2string(np.array(f(t,y).diff(t)).T[0],separator=', ')).replace('Matrix(',''))+'\n'+\
    'def p2fpt2(t,y):\n\treturn np.array(%s)'%(str(np.array2string(np.array(f(t,y).diff(t).diff(t)).T[0],separator=', ')).replace('Matrix(',''))+'\n'+\
    'def J(t,y):\n\treturn np.array(%s)'%(str(f(t,y).jacobian(y)).replace('Matrix(',''))+'\n'+\
    'def model(t,y):\n\treturn np.array(%s)'%(str(np.array2string(np.array(f(t,y)).T[0],separator=', ')).replace('Matrix(',''))+'\n'+\
    'def pJpt(t,y):\n\treturn np.array(%s)'%(str(f(t,y).jacobian(y).diff(t)).replace('Matrix(',''))

exec(A.replace('))',')',100))

# y00=np.array([1,0,1])

Time=np.array([])
Y = np.empty((0,n),np.float32)
from numpy.linalg import norm


N=0
while True:
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
    print('итерация',N,len(Y))
    if N>=3:
        YY=Y
        YO=OldY
        if len(YY)%2!=0:
            YY=YY[:-1]
        if len(YO)%2!=0:
            YO=YO[:-1]
        YY=np.array(YY,dtype=np.float32)
        YO=np.array(YO,dtype=np.float32)
        delta=np.max(norm(YY[0::2]-YO,axis=0))
        print('погрешность',delta)
        if N>10*2:
            break
        if delta<eps:
            break
# print(h)
solve = solve_ivp(model,[Tn0,tmax0],y00,method='LSODA',min_step=0.01,max_step=0.01)

Time2=solve.t
Z=solve.y

Z1,Z2=Z
Y1,Y2=Y.T


plt.subplot(131)
plt.plot(Time,Y1)
plt.plot(Time2,Z1)
plt.subplot(132)
plt.plot(Time,Y2)
plt.plot(Time2,Z2)
plt.subplot(133)
plt.plot(Z1,Z2)
plt.plot(Y1,Y2)
plt.show()


from scipy import interpolate

x = np.linspace(np.min(Time), np.max(Time),1000)
f = interpolate.interp1d(Time, Y1,axis=0, fill_value="extrapolate")
Y1f=f(x)
f = interpolate.interp1d(Time2, Z1,axis=0, fill_value="extrapolate")
Z1f=f(x)

plt.plot(x,Z1f-Y1f)
plt.show()

x = np.linspace(np.min(Time), np.max(Time),1000)
f = interpolate.interp1d(Time, Y2,axis=0, fill_value="extrapolate")
Y2f=f(x)
f = interpolate.interp1d(Time2, Z2,axis=0, fill_value="extrapolate")
Z2f=f(x)

plt.plot(x,Z2f-Y2f)
plt.show()