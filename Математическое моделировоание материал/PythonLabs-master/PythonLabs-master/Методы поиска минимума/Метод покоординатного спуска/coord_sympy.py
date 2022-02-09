from sympy import Symbol,diff,exp,cos,sin

x,y=Symbol('x[0]'),Symbol('x[1]')
f=x**2*y-10*x**2+4*x*y-40*x+y**3-30*y**2+295*y-949


print([[diff(f,x,x),diff(f,x,y)],[diff(f,y,x),diff(f,y,y)]])