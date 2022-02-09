from numpy import cos,sin,pi,log,linspace,array
from matplotlib import pyplot as plt
from trapzint import trapz

a,b=1,3
inteps=0.01 # Относительная погрешность

def F(i,t):
	return log(log(10+i+cos(t)))

def coeff(i,j):
	return(j**2+sin(j)**2)/log(1+j+i)

def sila(i):
	def Fi(t):
		return F(i,t)
	return trapz(Fi,a,b,inteps)

def f(t):
	return F(2,t)

plt.title('График подинтегральной функции для i=2')
plt.plot(linspace(a,b,100),f(linspace(a,b,100)))
plt.show()
trapz(f,a,b,inteps/100000,plot=True)

B=array([sila(i) for i in range(1,100)])
plt.title('График правой части уравнения')
plt.plot(B,'-')
plt.show()