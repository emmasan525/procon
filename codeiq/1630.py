import math

def countseven(n):
	seven=0
	while True:
		keta=int(math.log10(n) + 1)-1
		m=n/(10**keta)
		seven+=m*keta*(10**(keta-1))
		if m>7:
			seven+=10**keta
		elif m==7:
			seven+=n-(7*(10**keta))+1
		n=n%(10**keta)
		if n==0:
			break
	return int(seven)

try:
	while True:
		kazu=input()
		print countseven(kazu)
except EOFError:
	        pass


