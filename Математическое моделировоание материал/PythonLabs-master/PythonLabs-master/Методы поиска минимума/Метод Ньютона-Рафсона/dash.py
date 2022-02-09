# import pylab
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import sqrt,exp
# import math
import matplotlib.pyplot as plt
# import sympy as sym
x0=np.array([-9, 7])

def f(x):
    return ((x[0] + x[1]**2 - 12*x[1] + 45)*exp(x[0]/2))*exp(9/2)

def pr1(x):
    return exp(9/2)*(x[0] + x[1]**2 - 12*x[1] + 45)*exp(x[0]/2)/2 + exp(9/2)*exp(x[0]/2)
def pr2(x):
    return exp(9/2)*(2*x[1] - 12)*exp(x[0]/2)

def pr11(x):
    return exp(9/2)*(x[0]/4 + x[1]**2/4 - 3*x[1] + 49/4)*exp(x[0]/2)
def pr22(x):
    return 2*exp(9/2)*exp(x[0]/2)
def pr12(x):
    return exp(9/2)*(x[1] - 6)*exp(x[0]/2)
def pr21(x):
    return exp(9/2)*(x[1] - 6)*exp(x[0]/2)

epsilon=1e-3
k=0
xk=x0
X=[[],[]]

# normf=5
p=[[10],[10]] #произвольный начальный вектор


while np.linalg.norm(xk-p)>epsilon:
    k+=1
    X[0].append(xk[0])
    X[1].append(xk[1])

    grad=[[0],[0]]
    grad[0]=pr1(xk)
    grad[1]=pr2(xk)

    gess=[[0,0],[0,0]]
    gess[0][0]=pr11(xk)
    gess[0][1]=pr12(xk)
    gess[1][0]=pr21(xk)
    gess[1][1]=pr22(xk)


    if np.linalg.det(gess)!=0:
        invgess=np.linalg.inv(gess)
        pk=-np.dot(invgess,grad)
        pk=pk/np.linalg.norm(pk)


    # Нижняя граница отрезка унимодальности 0, а верхняя будет alpha0
    alpha0=0
    # Ширина окна выбирается из интуиции исследователя
    window_width=0.005
    N=0
    while not((f(xk+(alpha0-window_width)*pk)>f(xk+(alpha0)*pk))&(f(xk+(alpha0)*pk)<f(xk+(alpha0+window_width)*pk))):
        N+=1
        if N>10**5:
            break
        if f(xk+(alpha0-window_width)*pk)>f(xk+(alpha0+window_width)*pk):
            alpha0=alpha0+window_width/2
        else:
            alpha0=alpha0-window_width/2
    # print(alpha0)
    # золотое сечение
    l=0
    r=alpha0
    eps=0.0001

    phi = 0.5 * (1.0 + sqrt(5.0))
    t = (r-l)/phi

    alpha1 = r-t 
    alpha2 = l+t

    f1 = f(xk+alpha1*pk)
    f2 = f(xk+alpha2*pk)

    while abs(r - l) > eps:
      if f1 < f2:
        t = (r-l)/phi
        r = alpha2
        alpha2 = alpha1
        f2 = f1
        alpha1 = r-t
        f1 = f(xk+alpha1*pk)
      else:
        t = (r-l)/phi
        l = alpha1
        alpha1 = alpha2
        f1 = f2
        alpha2 = l+t
        f2 = f(xk+alpha2*pk)
    alpha=abs(alpha1+alpha2)/2
    # print(alpha)
    p=xk
    xk=xk+alpha*pk
# print(xk,k)

def makedata():
    x1=np.arange(-20,20,0.1)
    x2=np.arange(-20,20,0.1)
    x1grid,x2grid=np.meshgrid(x1,x2)
    zgrid=(x1grid+x2grid**2-12*x2grid+45)*np.exp((9+x1grid)/2)
#     zgrid=x1grid**2+x2grid**2
    return x1grid,x2grid,zgrid

# x1,x2,z=makedata()
# fig=pylab.figure()
# axes=Axes3D(fig)
# axes.plot_surface(x1,x2,z)
# plt.show()
X1=X[0]
X2=X[1]
x1,x2,z=makedata()
plt.plot(X1,X2,'ko-',markersize=1)
plt.contour(x1,x2,z)
plt.show()
print('Minima found:',xk,' steps:',k)