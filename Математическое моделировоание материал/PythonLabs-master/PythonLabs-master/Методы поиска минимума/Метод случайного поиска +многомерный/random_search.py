import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp,array
import matplotlib.pyplot as plt

def f(x):
    x=array(x).T
    return cos(x[0])*sin(x[1])

x=array([-4.9,0.41])

n=2

xmin,xmax=-6,-2
ymin,ymax=-1,3

d=0.01
eps1=0.0001

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 12
plt.rcParams["figure.figsize"] = fig_size

X=np.arange(xmin,xmax, 0.10)
Y=np.arange(ymin,ymax, 0.10)
X, Y = np.meshgrid(X, Y)   
plt.contour(X,Y,f(array([Y,X]).T),140)
plt.plot(x[0],x[1],'ro')

i=0
while d>eps1:
    xo = x
    psi=np.random.uniform(0, 2*pi)
    h=d*array([cos(psi), sin(psi)])
    x=x+h

    if f(x)>f(xo):
        d=d-0.01*d
        x=xo

    if f(x)<f(xo):
        d=d+0.01*d
        plt.plot([xo[0], x[0]],[xo[1], x[1]],'-r')

print('Iteration count: ',i)
plt.plot(x[0],x[1],'-bo')
print(x)
plt.show() 