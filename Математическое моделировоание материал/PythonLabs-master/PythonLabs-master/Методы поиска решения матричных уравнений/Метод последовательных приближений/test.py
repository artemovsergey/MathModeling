import numpy as np
from numpy import cos,sin,pi,log
from matplotlib import pyplot as plt
from numpy.linalg import inv,norm,det,solve,cond
from scipy.optimize import minimize

n=2
epsilon=0.1e-3
A=np.array([[1,1],[0,epsilon]])
b=np.array([2,epsilon**2])
E=np.identity(n)

def conde(epsilon):
	return cond(np.array([[1,1],[0,epsilon]]))
print(cond(A))
C=det(A)

aa=np.linspace(-0.01,0.01,1000)
bb=[conde(A) for A in aa]
plt.plot(aa,bb)
plt.show()

# (B.T@B+alpha*E)z=B.T@v

# 
B=A.T@A
v=A.T@b
print(B,v)

print(solve(B,v))
# Псевдорешение
def z(alpha):
	return inv(B.T@B+alpha*E)@(B.T@v)

# Невязка псевдорешения
def r(alpha):
	return norm(A@z(alpha)-b)

Alpha=minimize(r,0.5,method='Nelder-Mead').x

x=z(Alpha)
# A=np.linspace()

# ответ 
print(Alpha)
a=np.linspace(-1,1,10000)
b=[r(A) for A in a]
plt.plot(a,b)
plt.show()
print(x)
# print(A@x-b)
# print(r(Alpha))
# if det(A)!=0: