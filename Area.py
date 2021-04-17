def Area(A,B,C,D,Di):
'''float:::>float

this function gets the length and calculates the area of a three or four side shape'''

    if D==0:
        p=(A+B+C)/2
        print ((p*(p-A)*(p-B)*(p-C))**0.5)
    else:
        pABDi=(A+B+Di)/2
        pCDDi=(C+D+Di)/2
        Area1=((pABDi*(pABDi-A)*(pABDi-B)*(pABDi-Di))**0.5)
        Area2=((pCDDi*(pCDDi-C)*(pCDDi-D)*(pCDDi-Di))**0.5)
        print (Area1+Area2)
    
