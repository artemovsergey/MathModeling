from numpy import cos,sin,pi,log,sort,inf,linspace,abs,sum,append
from matplotlib import pyplot as plt

trap=[]
trapf=[]
def trapz(f,a,b,eps,integ0=inf,S=[],it=0,plot=False):
	if len(S)==0:
		S=linspace(a,b,3)
	h=S[1]-S[0]
	integ=sum([(f(S[i])+f(S[i+1]))/2*h for i in range(0,len(S)-1)])
	if abs((integ-integ0)/integ)>eps:

		Snew=S
		for i in range(0,len(S)-1):
			Snew=append(Snew,(S[i+1]+S[i])/2)
		Snew=sort(Snew)
		if plot:
			trap.append(it)
			trapf.append(integ)
		return trapz(f,a,b,eps,integ0=integ,S=Snew,it=it+1,plot=plot)
	else:
		if plot==True:
			plt.title('Значение интеграла от номера итерации при i=2')
			plt.plot(trap,trapf,'o-')
			plt.show()
		return integ