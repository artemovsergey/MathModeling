import numpy as np
from numpy import cos,sin,pi,log
from matplotlib import pyplot as plt
from trapzint import trapz

from iterprog import printProgressBar
import time
start_time = time.time()
print('Сколько уравнений забивать?')
n = input()  # считываем строку и кладём её в переменную name
n=int(n)
a,b=1,3
inteps=0.01 # Относительная погрешность

def F(i,t):
	return log(log(10+i+cos(t)))

def coeff(i,j):
	return (j**2+sin(j)**2)/log(1+j+i)

def sila(i):
	def Fi(t):
		return F(i,t)
	return trapz(Fi,a,b,inteps)

print('Приступаю к расчету beta')
beta=np.array([sila(i)/(n**3-coeff(i,i)) for i in range(1,n+1)],dtype=np.float32)

print('Приступаю к расчету alpha')

t0= time.time()
A=np.zeros([n,n], dtype=np.float32)
import os
clear = lambda: os.system('cls')

for i in range(1,n+1):
	printProgressBar(i, n, prefix = 'Progress:', suffix = 'Complete', length = 50)
	ii=coeff(i,i)
	for j in range(1,n+1):
		if i==j:
			A[i-1][j-1]=0
		else:
			A[i-1][j-1]=coeff(i,j)/(n**3-ii)

t1= time.time()

print('Приступаю к расчету решения встроенной функцией')
E=np.identity(n)
x1=np.linalg.solve(E-A, beta)
t2= time.time()
np.save('data/alpha_arr_n'+str(n),A)
np.save('data/beta_arr_n'+str(n),beta)
np.save('data/x_arr_n'+str(n),x1)
print('\nВремя работы %s с'%(t2-t0))
