def Areax(A,B,C,D,Di):
    '''float:::>float

this function gets the length and calculates the area of a three or four side shape,no matter which side equals 0 , area of a triangle will be calculated.'''
    if D==0:
        if A+B>C and A+C>B and B+C>A:
            p=(A+B+C)/2
            print ((p*(p-A)*(p-B)*(p-C))**0.5)
         else:
             print ('none')
    elif C==0:
        if A+B>D and A+D>B and B+D>A:
            p=(A+B+D)/2
            print ((p*(p-A)*(p-B)*(p-D))**0.5)
        else:
            print('none')
    elif B==0:
        if A+C>D and A+D>C and C+D>A:
            p=(A+C+D)/2
            print ((p*(p-A)*(p-D)*(p-C))**0.5)
        else:
            print('none')
    elif A==0:
        if C+B>D and C+D>B and B+D>C:
            p=(D+B+C)/2
            print ((p*(p-D)*(p-B)*(p-C))**0.5)
        else:
            print('none')

    else:
        if A+B>Di and A+Di>B and B+Di>A and D+Di>C and D+C>Di and D+C>Di:
            pABDi=(A+B+Di)/2
            pCDDi=(C+D+Di)/2
            Area1=((pABDi*(pABDi-A)*(pABDi-B)*(pABDi-Di))**0.5)
        Area2=((pCDDi*(pCDDi-C)*(pCDDi-D)*(pCDDi-Di))**0.5)
        print (Area1+Area2)

