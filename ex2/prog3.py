def prog3(a):
	if a in [1,2]:
		return True
	for x in range(2,a):
		if a%x ==0:
			return False
	return True
