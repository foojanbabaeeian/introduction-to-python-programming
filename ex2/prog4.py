def prog4(a):
	l=[]
	if a<=0:
		return l
	elif a==1:
		return [1]
	for x in range(1,a+1):
		if a%x ==0:
			l.append(x)
	return l
