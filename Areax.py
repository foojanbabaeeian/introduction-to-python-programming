def Areax(A,B,C,D,Di):
    '''float:::>float

this function gets the length and calculates the area of a three or four side shape,no matter which side equals 0 , area of a triangle will be calculated.'''

    if A or B or C or D==0:
        if D==0:
            p=(A+B+C)/2
            print ((p*(p-A)*(p-B)*(p-C))**0.5)
        elif C==0:
            p=(A+B+D)/2
            print ((p*(p-A)*(p-B)*(p-D))**0.5)
        elif B==0:
            p=(A+C+D)/2
            print ((p*(p-A)*(p-D)*(p-C))**0.5)
        else:
            p=(D+B+C)/2
            print ((p*(p-D)*(p-B)*(p-C))**0.5)
            
    elif A or B or C or D!=0:
        pABDi=(A+B+Di)/2
        pCDDi=(C+D+Di)/2
        Area1=((pABDi*(pABDi-A)*(pABDi-B)*(pABDi-Di))**0.5)
        Area2=((pCDDi*(pCDDi-C)*(pCDDi-D)*(pCDDi-Di))**0.5)
        print (Area1+Area2)
    
