def sosu(s,a,sosudayo):
	if s%2==0:
		s=s+1
	for i in range (s,a,2):
		j=0
		b=True
		while sosudayo[j]**2<=i:
			if i%sosudayo[j]==0:
				b=False
				break
			j+=1
		if b:
			sosudayo.append(i)
	return sosudayo

start=3
sosulist=[2]
try:
	while True:
		kazu=input()
		sosulist=sosu(start,kazu,sosulist)
		if kazu==2:
			print 0
		else:
			print len(sosulist)
		start=kazu
except EOFError:
	        pass


