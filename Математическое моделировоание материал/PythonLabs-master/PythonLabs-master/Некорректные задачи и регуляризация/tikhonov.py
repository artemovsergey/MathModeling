import numpy as np
from numpy import cos,sin,pi,log,sqrt
from matplotlib import pyplot as plt
from numpy.linalg import inv,norm,det,solve,cond,pinv
from scipy.optimize import minimize

n=2

epsilon=0.001
h,delta=0.01,0.01


A=np.array([[1,1],[0,epsilon]])
b=np.array([2,epsilon**2])
E=np.identity(n)
print(A,b)
print(solve(A,b))
# def conde(epsilon):
	# return cond(np.array([[1,1],[0,epsilon]]))
# print(cond(A))
# C=det(A)

# aa=np.linspace(-0.01,0.01,1000)
# bb=[conde(A) for A in aa]
# plt.plot(aa,bb)
# plt.show()

# (B.T@B+alpha*E)z=B.T@v

# 
B=A.T@A
v=A.T@b
# print(B,v)
# print(cond(B))

# print(solve(B,v))


# Псевдорешение
def z(alpha):
	try:
		return pinv(B.T@B+alpha*E)@(B.T@v)
	except:
		print('Pseudosolve existn`t')
		# return pinv(A.T@A+alpha*E)@(A.T@b)
		# print(B.T@B+alpha*E)
		# return [[0,0],[0,0]]


# Классическая невязка псевдорешения
def r(alpha):
	return norm(B@z(alpha)-v)**2

# eta -- мера несовместности
def f(z):
    return norm(B@z-v)
zm = minimize(f, [0, 0]).x # 
eta=norm(B@zm-v)
print('eta^2',eta**2)
# Обобщенная невязка псевдорешения
def obobr(alpha):
	a=(norm(B@z(alpha)-v)**2-(delta+h*norm(z(alpha)))**2-eta**2)
	# print('a',a)
	return a
# h,delta=0.5,0.5

if norm(v)**2>delta**2+eta**2:
	print('Условие принимения приницпа обобщенной невязки выполено')
else:
	print('Решение %s'%(b*0))
	import sys
	sys.exit()


# Alpha=minimize(r,0.5,method='Nelder-Mead').x
Alpha=minimize(obobr,0,method='Nelder-Mead').x
print(Alpha, r(Alpha), obobr(Alpha))

print('Ответ',z(Alpha))

# A=np.linspace()

# ответ 
# a=np.linspace(-1400,-1300,10000)
# b=[obobr(A) for A in a]
# plt.plot(a,b)
# plt.show()
# print(A@x-b)
# print(r(Alpha))
# if det(A)!=0: