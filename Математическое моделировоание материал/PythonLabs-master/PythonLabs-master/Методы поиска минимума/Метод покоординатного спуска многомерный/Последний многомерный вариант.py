import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
import matplotlib.pyplot as plt

def f(x,y):
	return -(-(x**2)/3 - x*y/6 + 19*x/2 - (y**2)/3 + 16*y + 235/3)

#вычисляем из формулы для золотого сечения
phi = 0.5 * (1.0 + sqrt(5.0))

#золотое сечение
def minimize(f,eps,a,b,X,par): 
	dd=abs(f(b,par)-f(a,par))
	if X:
		dd=abs(f(par,b)-f(par,a))
	if dd < eps: 
		return (a+b)/2
	else:
		t = (b-a)/phi
		x1, x2 = b - t, a + t
		q=f(x1,par)
		Q=f(x2,par)
		if X:
			q=f(par,x1)
			Q=f(par,x2)
		if q>=Q:
			return minimize(f, eps, x1, b,X,par)
		else:
			return minimize(f, eps, a, x2,X,par)
		
def scrola(f,x0):
	h=0.5
	N=0
	while not((f(x0-h)>f(x0))&(f(x0)<f(x0+h))):
		if N>10**3:
			print('bl!')
			break
		N+=1
		if f(x0-h)>f(x0+h):
			x0=x0+h/2
		else:
			x0=x0-h/2
	return x0


xmin,xmax=0,30
ymin,ymax=0,30
x0,y0=29,19
eps=0.0001

X = np.arange(xmin,xmax, 0.010)
Y = np.arange(ymin,ymax, 0.010)
X, Y = np.meshgrid(X, Y)

plt.contour(X,Y,f(X,Y),50)
plt.plot(x0,y0,'bo')

i=xo=yo=0
while abs(f(xo,yo)-f(x0,y0))>eps:
	i+=1
	if i>10**3:
		print('break!')
		break
	xo,yo=x0,y0
	def ff(x):
		return f(x,y0)
	x0=minimize(f,eps,x0,scrola(ff,y0),False,y0)
	def ff(y):
		return f(x0,y)
	y0=minimize(f,eps,y0,scrola(ff,x0),True,x0)
	plt.plot([xo,xo,x0],[yo,y0,y0],'-b')

plt.plot(x0,y0,'ro')
print('Итераций: ', i)
print(x0,y0)
plt.show()