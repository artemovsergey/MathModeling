import numpy as np
from numpy import cos,sin,pi,log
from matplotlib import pyplot as plt
import time
start_time = time.time()

def DiagDominant(X):
	D = np.diag(np.abs(X)) # Find diagonal coefficients
	S = np.sum(np.abs(X), axis=1) - D # Find row sum without diagonal
	return np.all(D > S)

#2,4,10,100,1000,10000
n=10000
print('Количество уравнений %s' % n)
alpha=np.load('data/alpha_arr_n'+str(n)+'.npy') 
beta=np.load('data/beta_arr_n'+str(n)+'.npy') 
x1=np.load('data/x_arr_n'+str(n)+'.npy')
# A=np.load('A_arr_n'+str(n)+'.npy') 
# b=np.load('b_arr_n'+str(n)+'.npy') 

print('Матрицы загружены, командир')
if np.linalg.norm(alpha,ord=1):
	print('Должно сойтись')
# print(alpha,beta)
# print(A,b)
# import sys
# sys.exit()

eps=0.001

# Xk=np.zeros(n)
Xk=beta
Xkk=np.ones(n)*10e9
E=np.identity(n)
# T=E-A

# H=1/np.linalg.norm(A,ord=1)*E



t1=time.time() - start_time

# normT=np.linalg.norm(T,ord='fro')
# pr/int(normT)
# epsa=eps*(1-normT)/normT
# print(epsa)
# print(alpha)
# print('---')
N=0
norms=[]
while np.linalg.norm(Xk-Xkk)/np.linalg.norm(Xkk)>eps:
	N+=1
	# print()
	norms.append(np.linalg.norm(Xk))
	Xkk=Xk
	Xk=alpha@Xkk+beta
plt.title('График зависимости нормы решения от номера итерации')
plt.tight_layout()
plt.plot(norms,'-o')
plt.show()
print('Количество итераций %s'%N)
print(np.linalg.norm(Xk), np.linalg.norm(x1))
# t2=time.time() - start_time
# # print('Iteration count: ',i, ', final point: ',x,', function at final point: ',f(x))
# print("Время инициализации %s с, время цикла %s с, суммарное время %s с" % (t1,t2,t1+t2))

# # print(np.dot(A,Xk)-b)