def func4(x):
    OutputList = []
    for a in x:         
        OutputList.append(prog4(a))
    return OutputList
def prog4(a):
    l=[]
    if a[0]>a[1]:
        max = a[0]
        min = a[1]
    else:
        max = a[1]
        min = a[0]
    if a[0]<=0 or a[1]<=0:
            return l
    elif a[0]==1 or a[1]==0:
            return [1]
    for x in range(1,max+1):
            if a[0]%x ==0 and a[1]%x==0:
                    l.append(x)
    return (int(a[0]/ l[-1]), int(a[1]/ l[-1]))
