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
		return 10#n**3-(j**2+sin(j)**2)/log(1+j+i)
	else:
		return 1#-(j**2+sin(j)**2)/log(1+j+i)

def sila(i):
	def Fi(t):
		return F(i,t)
	return 10#trapz(Fi,a,b,inteps)

def trapz(f,a,b,eps,integ0=np.inf,S=[]):
	if len(S)==0:
		S=np.linspace(a,b,3)
	h=S[1]-S[0]
	integ=np.sum([(f(S[i])+f(S[i+1]))/2*h for i in range(0,len(S)-1)])
	if np.abs((integ-integ0)/integ)>eps:

		Snew=S
		for i in range(0,len(S)-1):
			Snew=np.append(Snew,(S[i+1]+S[i])/2)
		Snew=np.sort(Snew)

		return trapz(f,a,b,eps,integ0=integ,S=Snew)
	else:
		return integ

n=3
print('Приступаю к расчету b')
b=np.array([sila(i) for i in range(1,n+1)],dtype=np.float32)
print('Приступаю к расчету A')
# A=np.array([[coeff(i,j) for i in range(1,n+1)] for j in range(1,n+1)],dtype=np.float32)

t0= time.time()
# A=np.array([[coeff(i,j) for j in range(1,n+1)] for i in range(1,n+1)],dtype=np.float32)
# t1= time.time()
# print(t1-t0)
# # print(A)
# t0= time.time()
A=np.zeros([n,n], dtype=np.float32)

for i in range(1,n+1):
	print(i, t0-time.time())
	for j in range(1,n+1):
		A[i-1][j-1]=coeff(i,j)
# A=np.array([[1 for i in range(1,n+1)] for j in range(1,n+1)],dtype=np.float32)
t1= time.time()
print(t1-t0)
# print(A)

np.save('A_arr_n'+str(n),A)
np.save('b_arr_n'+str(n),b)
# t2 = time.time()-start_time
# print("Время инициализации %s с, время подсчета интегралов %s с, суммарное время %s с" % (t1,t2,t1+t2))