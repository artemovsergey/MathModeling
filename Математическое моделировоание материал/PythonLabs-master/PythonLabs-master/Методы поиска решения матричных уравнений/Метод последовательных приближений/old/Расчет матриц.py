import numpy as np
from numpy import cos,sin,pi,log
from matplotlib import pyplot as plt
import time
start_time = time.time()
n=10000
a,b=1,3
inteps=0.01 # Относительная погрешность

def F(i,t):
	return log(log(10+i+cos(t)))

def norm2(Arr):
	return np.sqrt(np.sum(np.abs(Arr)**2))

def coeff(i,j):
	if i==j:
		return n**3-(j**2+sin(j)**2)/log(1+j+i)
	else:
		return -(j**2+sin(j)**2)/log(1+j+i)

def sila(i):
	def Fi(t):
		return F(i,t)
	return trapz(Fi,a,b,inteps)
t1 = time.time()-start_time
trap=[]
trapf=[]

def trapz(f,a,b,eps,integ0=np.inf,S=[],it=0,plot=False):
	if len(S)==0:
		S=np.linspace(a,b,3)
	h=S[1]-S[0]
	integ=np.sum([(f(S[i])+f(S[i+1]))/2*h for i in range(0,len(S)-1)])
	if np.abs((integ-integ0)/integ)>eps:

		Snew=S
		for i in range(0,len(S)-1):
			Snew=np.append(Snew,(S[i+1]+S[i])/2)
		Snew=np.sort(Snew)
		if plot:
			trap.append(it)
			trapf.append(integ)
		return trapz(f,a,b,eps,integ0=integ,S=Snew,it=it+1,plot=plot)
	else:
		if plot==True:
			plt.plot(trap,trapf,'o-')
			# plt.show()
		return integ

# Задание 3
def f(t):
	return F(2,t)
plt.plot(np.linspace(a,b,100),f(np.linspace(a,b,100)))
# plt.show()
trapz(f,a,b,inteps/100000,plot=True)

B=np.array([sila(i) for i in range(1,100)])
# Задание 4
plt.plot(B,'-')
# plt.show()

# Задание 5
# 	Ax=b
eps=0.001
A=np.array([[coeff(i,j) for i in range(1,n+1)] for j in range(1,n+1)],dtype=np.float32)
b=np.array([sila(i) for i in range(1,n+1)],dtype=np.float32)
np.save('A_arr_n'+str(n),A)
np.save('b_arr_n'+str(n),b)
t2 = time.time()-start_time
print("Время инициализации %s с, время подсчета интегралов %s с, суммарное время %s с" % (t1,t2,t1+t2))