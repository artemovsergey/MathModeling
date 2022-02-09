#многомерный метод случайного поиска 
from numpy import sqrt,sum,pi,cos,sin,zeros,copy
from numpy.random import uniform
# import matplotlib.pyplot as plt 
n=5 #размерность пространства 
x0=[uniform(0,3) for i in range(n)] # начальный вектор 

eps=0.0001 # точность
h=0.01 # шаг 
pi=3.14159265 
k=0

# f- задаваемая функция 
def f(x): 
	return sqrt(sum([x[i]**2 for i in range(n)])) 

# произведение синусов фи, начиная с i-го и заканчивая m-ым 
def psin_i(phi,i,m): 
	p=1
	pk=1
	for k in range(i,m+1): 
		pk=sin(phi[k]) 
	# print(pk,x[k]) 
	p=p*pk 
	return p


def genphi():
	phi=zeros(2*n) # а пусть с запасом... побольше будет)) 
	# Генерируем фи, прямо по википедии. Внимание, 
	# нумеровать элементы массива буду с единички, 
	# а нулевой элемент c особым смыслом - это будет cos(alpha0)=1,
	# чтобы формула из вики была одинаковая для всех x
	phi[0]=0
	for i in range(1,n-2+1):
		phi[i]=uniform(0,pi) 
	phi[n-1]=uniform(0,2*pi) 
	return phi

x=x0 
while (h > eps) & (k<10000): 
	k+=1 
	x0=copy(x) 
	
	phi=genphi()

	# Шагание
	for i in range(n): 
		x[i]=x[i]+h*cos(phi[i])*psin_i(phi,i+1,n-1)

	if f(x)>f(x0): 
		h=0.99*h
		x=copy(x0)
	elif f(x)<f(x0): 
		h=1.01*h

print('точка минимума:',x,'шагов:',k)