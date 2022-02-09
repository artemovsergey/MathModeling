import scipy.integrate as spint
from numpy import cos,sin,exp, log as ln
import numpy as np
from numpy.linalg import inv,norm,cond,solve

n=3
A=np.array([[1,4,6],[8,3,6],[1,2,3]])
b=np.array([2,2,4])

# Добавляем лишние элементы в массив, чтобы 
# нумерация  элементов совпадала с методичкой

b=np.hstack([0,b])
d=np.hstack([0,np.diag(A,k=0)])
c=np.hstack([0,np.diag(A,k=1)])
a=np.hstack([0,0,np.diag(A,k=-1)])

# print(d,c,a)
print(A)
L=np.zeros(n+2)
M=np.zeros(n+2)

L[2]=-c[1]/d[1]
M[2]=b[1]/d[1]
print(M[2],L[2])
for N in range(3,n+1):
	i=N-1
	L[N]=-c[i]/(a[i]*L[i]+d[i])
	M[N]=(b[i]-M[i]*a[i])/(a[i]*L[i]+d[i])
# print(M)
# print(L)

x=np.zeros(n+1)
x[n]=(b[n]-M[n]*a[n])/(a[n]*L[n]+d[n])

for i in range(n-1,0,-1): # n, n-1, ..., 1
	print(i)
	x[i]=x[i+1]*L[i+1]+M[i+1]

# Обрезаем лишний нолик 
x=x[1:]
b=b[1:]
print('')
print(x)
print(solve(A,b))