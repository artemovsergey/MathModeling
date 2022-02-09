import numpy as np
from numpy import cos,sin,pi,log
from matplotlib import pyplot as plt
import time
start_time = time.time()

def DiagDominant(X):
	D = np.diag(np.abs(X)) # Find diagonal coefficients
	S = np.sum(np.abs(X), axis=1) - D # Find row sum without diagonal
	return np.all(D > S)

#2,10,100,1000,2000,10000
n=10
A=np.load('A_arr_n'+str(n)+'.npy') 
b=np.load('b_arr_n'+str(n)+'.npy') 

print('Матрицы загружены, командир')
print(DiagDominant(A))
import sys
sys.exit()

eps=0.001

Xk=np.zeros(n)
Xk=b
Xkk=np.ones(n)*10e9
E=np.identity(n)
T=E-A
N=0

H=1/np.linalg.norm(A,ord=1)*E

x1=np.linalg.solve(A, b)

t1=time.time() - start_time

normT=np.linalg.norm(T,ord='fro')
print(normT)
epsa=eps*(1-normT)/normT
print(epsa)
# while np.linalg.norm(Xk-Xkk)>eps:
# 	# print(N)
# 	if N>10**2:
# 		break
# 	N+=1
# 	Xkk=Xk
# 	# Xk=T@Xkk+b
# 	# Xk=Xkk+np.dot(H,(b-np.dot(A,Xkk)))
# 	Xk=Xkk+H@(b-A@Xkk)
# print(Xk,N,'\n',x1)
# t2=time.time() - start_time
# # print('Iteration count: ',i, ', final point: ',x,', function at final point: ',f(x))
# print("Время инициализации %s с, время цикла %s с, суммарное время %s с" % (t1,t2,t1+t2))

# # print(np.dot(A,Xk)-b)