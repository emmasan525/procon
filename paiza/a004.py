lines = raw_input().split()
amida=[[0 for i in range(int(lines[0]))] for j in range(int(lines[1]))]

for i in xrange(int(lines[2])):
	s=raw_input().split()
	amida[(int(s[0]))-1][int(s[1])]=1*int(s[2])
	amida[int(s[0])][int(s[2])]=-1*int(s[1])

p=0
c=int(lines[0])-1
while c>0:
	if amida[p][c]>0:
		c=amida[p][c]-1
		p=p+1
	elif amida[p][c]<0:
		c=abs(amida[p][c])-1
		p=p-1
	else:
		c=c-1

print p+1

