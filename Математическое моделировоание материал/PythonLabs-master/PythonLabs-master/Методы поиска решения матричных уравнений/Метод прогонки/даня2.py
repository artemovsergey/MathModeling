
d,c,a=np.diag(A,k=0),np.diag(A,k=1),np.diag(A,k=-1)

def L(n):
	if n==2:
		return -c[0]/d[0]
	else:
		i=n-1
		return -c[i-1]/(a[i-2]*L(i)+d[i-1])

def M(n):
	if n==2:
		return b[0]/d[0]
	else:
		i=n-1
		return (b[i-1]-M(i)*a[i-2])/(a[i-2]*L(i)+d[i-1])

x=np.zeros(n)
x[n-1]=(b[n-1]-M(n)*a[n-2])/(a[n-2]*L(n)+d[n-1])

for i in reversed(range(0,n-1)): # n, n-1, ..., 1
	x[i-1]=x[i]*L(i+1)+M(i+1)

print(x)