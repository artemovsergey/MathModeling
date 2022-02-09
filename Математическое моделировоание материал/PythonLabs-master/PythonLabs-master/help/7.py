
# coding: utf-8

# In[1]:


from numpy import cos,sin,exp,sqrt,sum,abs, log as ln
import numpy as np
from numpy.linalg import inv,norm,cond,solve

# подинтегральная функция
def f(i,t):
    return exp(-i**2*t)/(1+i*t*sin(t)**2)

def T(N,f,a,b):
    if N==0:
        return (b-a)/2*(f(a)+f(b))
    else:
        g=2**N
        M=int(g/2)
        h=(b-a)/g
        def xk(k):
            return a+k*h
        return T(N-1,f,a,b)/2+h*sum([f(xk(2*k+1)) for k in range(1,M+1)])

def S(N,f,a,b):
    return (4*T(N,f,a,b)-T(N-1,f,a,b))/3

def B(N,f,a,b):
    return (16*S(N,f,a,b)-T(N-1,f,a,b))/15

def getIntegral(f,a,b,eps,plot=False):
    N=2
    int1=B(1,f,a,b)
    int2=B(2,f,a,b)
    # ARR=[]
    # ARR.append(int2)
    while abs(int2-int1)/abs(int2)>eps:
        N+=1
        int1=int2
        int2=B(N,f,a,b)
        # ARR.append(int2)
    # if plot==False:
    return int2 
    # else:
        # return np.array(ARR)

n=100

# Матрицы Ax=b
A=np.zeros([n,n],dtype=np.float32)
for j in range(0,n):
    i=j+1
    A[j][j]=-(6*i**2+3)
for j in range(1,n-1):
    i=j+1
    A[j][j-1]=(2*i+1)
    A[j][j+1]=(4*i+2)
A[0][0]=A[n-1][n-1]=1
A[0][1]=-0.1
A[n-1][n-2]=-0.5

print('end fill A')
b=np.zeros(n,dtype=np.float32)
for j in range(1,n-1):
    epsi=0.01
    print(j)
    def rightIntegral(t):
        return f(j+1,t)
    b[j]=getIntegral(rightIntegral,0,1,epsi)
    
d,c,a=np.diag(A,k=0),np.diag(A,k=1),np.diag(A,k=-1)
M,L,x=np.zeros(n),np.zeros(n),np.zeros(n)
# Прямая прогонка 
for i in range(0,n-1):
    if i==0:
        L[i]=-c[0]/d[0]
        M[i]=b[0]/d[0]
    else:
        L[i]=-c[i]/(a[i-1]*L[i-1]+d[i])
        M[i]=(b[i]-M[i-1]*a[i-1])/(a[i-1]*L[i-1]+d[i])
        

# Обратная прогонка 
x[n-1]=(b[n-1]-M[n-2]*a[n-2])/(a[n-2]*L[n-2]+d[n-1])

for i in reversed(range(0,n-1)):
    x[i]=x[i+1]*L[i]+M[i]

x9=solve(A,b)

print(norm(x))
print(norm(x9))
# print(len(x))
# print(x)
# print(M)
# print(A)

