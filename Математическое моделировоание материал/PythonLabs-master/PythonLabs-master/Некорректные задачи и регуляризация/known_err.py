import numpy as np
from numpy import cos,sin,pi,log,sqrt,trace as Trace
from matplotlib import pyplot as plt
from numpy.linalg import inv,norm as Norm,det,solve,cond,pinv
from scipy.optimize import minimize

n=2
epsilon=0.00000

A=np.array([[1,1],
			[0,epsilon]])

b=np.array([2,
			epsilon**2])
I=np.identity(n)

AT=A.T
A=AT@A
b=AT@b

def z(alpha):
	return inv(A.T@A+alpha*I)@(A.T@b)

# The generalized cross-validation 
# (does not depend on a priori information about noise δ)
def G(alpha):
	return Norm((I-A@inv(A.T@A+alpha*I)@A.T)@b)**2/\
				Trace(I-A@inv(A.T@A+alpha*I)@A.T)**2

alpha = minimize(G, [-1/2]).x

print('Regular solve',z(alpha))
try:
	print('Solve',inv(A)@b)
except:
	print('Pseudosolve',pinv(A)@b)