# Заполнение матриц
A=np.identity(n)
diag1,diag2 = np.diagonal(A, -1),np.diagonal(A, 1)
diag1.setflags(write=True)
diag2.setflags(write=True)
diag1.fill(1)
diag2.fill(1)
A[0][1]=A[n-1][n-2]=0

for j in range(1,n-1):
	A[j][j]=coef(j+1)
print(A)
# ssssssssssssss