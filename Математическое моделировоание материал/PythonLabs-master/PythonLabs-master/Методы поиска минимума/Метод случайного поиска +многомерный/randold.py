import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
import matplotlib.pyplot as plt

def f(x,y):
    return cos(x)*sin(y)

x,y=-4.9,0.41
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
plt.contour(X,Y,f(X,Y),140)
plt.plot(x,y,'ro')
                   
i=0
while d>eps1:
    i+=1
    xo,yo=x,y
    psi=np.random.uniform(0, 2*pi)
    x=x+d*cos(psi)
    y=y+d*sin(psi)
    if f(x,y)>f(xo,yo):
        d=d-0.01*d
        x,y=xo,yo
    if f(x,y)<f(xo,yo):
        d=d+0.01*d
        plt.plot([xo, x],[yo, y],'-r')

print('Итераций: ',i)
plt.plot([x],[y],'-bo')
print(x,y)
plt.show() 