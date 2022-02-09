import time
start_time = time.time()

import operator
from math import cos,sin,pi
from random import uniform as Uniform
from functools import reduce

t1=time.time() - start_time

a = [1,2,3,4]
b = [10,11,12,13]

def scaldot(a,S):
	return list(map(lambda x: x*S, a))

def dot(a,b):
	if type(a) is float:
		if type(b) is float:
			return a*b
		else:
			return scaldot(b,a)
	elif type(b) is float:
		if type(a) is float:
			return a*b
		else:
			return scaldot(a,b)
	else:
		return list(map(operator.mul, a, b))
def summ(a,b):
	return list(map(operator.add, a, b))

def Cos(a):
	if type(a) is float:
		return cos(a)
	else:
		return  list(map(cos, a))

def Sin(a):
	if type(a) is float:
		return sin(a)
	else:
		return  list(map(sin, a))

def prod(iterable):
	return reduce(operator.mul, iterable, 1)

def f(x):
    #x=list(map(list, zip(*x))) # Transpose
    return dot(dot(dot(dot(Cos(x[0]),Sin(x[1])),Sin(x[2])),Sin(x[3])),Sin(x[4]))

def uniform(low, high, size):
	if size>0:
		return [Uniform(low, high) for _ in range(size)]
	else:
		return Uniform(low, high)

n=5
x=uniform(-10, 10,n)

d=0.01
eps1=0.0001

i=0
while d>eps1:
    i+=1
    if i>10**5:
        print('Exception: iteration overflow!')
        break
    xo = x
    psi,psi[0],psi[1]=uniform(0, pi,n),0,uniform(0, 2*pi,0)


    h=scaldot([cos(psi[i-1])*prod([sin(psi[k]) for k in range(i,n)]) for i in range(1,n+1)],d)
    # А.Ф. Никифоров, С.К.Суслов, В.Б.Уваров. Классические ортогональные полиномы дискретной переменной. 
    # М.:Наука, 1985, 161-я страница.

    x=summ(x,h)

    if f(x)>f(xo):
        d=d-0.01*d
        x=xo
    if f(x)<f(xo):
        d=d+0.01*d

t2=time.time() - start_time
print('Iteration count: ',i, ', final point: ',x,', function at final point: ',f(x))
print("Время импорта %s с, время работы %s с, суммарное время %s с" % (t1,t2,t1+t2))