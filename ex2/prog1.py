 def prog1(a,b):
	l=[]
	if a%2==0:
		a+=1
	for c in range (a+1,b,2):
		l.append(c)
	return l
