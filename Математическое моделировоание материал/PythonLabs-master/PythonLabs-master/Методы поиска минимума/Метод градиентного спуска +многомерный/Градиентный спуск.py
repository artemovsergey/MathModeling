# %matplotlib inline

import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
import matplotlib.pyplot as plt
from scipy import optimize

def f(x,y):
    return cos(x)*sin(y)#-x-y**2+y*sqrt(x-9)+18*y-6*sqrt(x-9)-63

def gradx(x,y):
    return -sin(x)*sin(y)#(-2*(3 + sqrt(-9 + x)) + y)/(2*sqrt(-9 + x))

def grady(x,y):
    return cos(x)*cos(y)#18 + sqrt(-9 + x) - 2*y

x0,y0=-6,1.57
x0,y0=-6,-1
x0,y0=-4.9,0.41


phi = 0.5 * (1.0 + sqrt(5.0))

def scw(f,h):
    x0=0
    while not((f(x0-h)>f(x0))&(f(x0)<f(x0+h))):
        if f(x0-h)>f(x0+h):
            x0=x0+h/2
        else:
            x0=x0-h/2
    return x0


def minimize(f,eps,a,b): 
    if abs(b - a) < eps: 
        return 0.5 * (a + b)
    else:
        t = (b - a) / phi
        x1, x2 = b - t, a + t
        if f(x1) >= f(x2):
            return minimize(f,eps,x1,b)
        else:
            return minimize(f,eps,a,x2)
            
def p(x,y):
    return np.array([-gradx(x,y), -grady(x,y)])
         
x,y=x0,y0

xmin,xmax=-8,2
ymin,ymax=-3,5


X = np.arange(xmin,xmax, 0.10)
Y = np.arange(ymin,ymax, 0.10)
X, Y = np.meshgrid(X, Y)

plt.contourf(X,Y,f(X,Y),20)
plt.plot(x0,y0,'ro')

feps=0.0001
xo,yo=-1000,-1000
h,eps=0.05,0.01

i=0
while sqrt((x-xo)**2+(y-yo)**2)>feps:
    i+=1
    def F(alpha):
        return f(x+alpha*(-gradx(x,y)),y+alpha*(-grady(x,y)))
    alpha=minimize(F,eps,0,scw(F,h))
    # A=np.linspace(0,100,5000)
    # # pi
    # plt.plot(A,F(A))
    # plt.plot(alpha,F(alpha),'ro')
    # plt.show()
    xo,yo=x,y
    x,y=x+alpha*(-gradx(x,y)),y+alpha*(-grady(x,y))
    plt.plot([xo, x],[yo, y],'-r')
    # print(alpha,x,y)
    # print(alpha,sqrt((x-xo)**2+(y-yo)**2))
print('Итераций: ',i)
plt.plot([x],[y],'-bo')
plt.show()