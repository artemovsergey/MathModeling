import numpy as np
from numpy import cos,sin,pi,log
from matplotlib import pyplot as plt
from trapzint import trapz
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
	return (j**2+sin(j)**2)/log(1+j+i)

def sila(i):
	def Fi(t):
		return F(i,t)
	return trapz(Fi,a,b,inteps)

n=10000
print('Приступаю к расчету beta')
beta=np.array([sila(i)/(n**3-coeff(i,i)) for i in range(1,n+1)],dtype=np.float32)
# beta=np.array([sila(i)/(coeff(i,i)) for i in range(1,n+1)],dtype=np.float32)
# print(beta)
print('Приступаю к расчету alpha')
# A=np.array([[coeff(i,j) for i in range(1,n+1)] for j in range(1,n+1)],dtype=np.float32)

t0= time.time()
# A=np.array([[coeff(i,j) for j in range(1,n+1)] for i in range(1,n+1)],dtype=np.float32)
# t1= time.time()
# print(t1-t0)
# # print(A)
# t0= time.time()
A=np.zeros([n,n], dtype=np.float32)
import os
clear = lambda: os.system('cls')

for i in range(1,n+1):
	if i%50==0:
		# clear()
		print(i, t0-time.time())
	ii=coeff(i,i)
	for j in range(1,n+1):
		if i==j:
			A[i-1][j-1]=0
		else:
			A[i-1][j-1]=coeff(i,j)/(n**3-ii)
			# A[i-1][j-1]=coeff(i,j)/(coeff(i,i))
# A=np.array([[1 for i in range(1,n+1)] for j in range(1,n+1)],dtype=np.float32)
t1= time.time()
# print(t1-t0)
# print(A)
# print(coeff(1,2)/(10**3-coeff(1,1)))
np.save('alpha_arr_n'+str(n),A)
np.save('beta_arr_n'+str(n),beta)
# t2 = time.time()-start_time
# print("Время инициализации %s с, время подсчета интегралов %s с, суммарное время %s с" % (t1,t2,t1+t2))