import random
#E stands for EVEN numbers
#O stands for ODD numbers
#ex :::> bEO is the amount of even numbers between an even and odd number
    '''int :::> none
this function gets two numbers and gives an even number randomly between them'''

def Rand2(a,b):
    if a==b:
        return None
    elif a>b:
        max = a
        min = b
    else:
        max = b
        min = a
    if (max - min == 1) or (max-min == 2 and max%2==0):
        return None
    else:
        bEO=(max-(min+1))/2
        bEE=(max-min-2)/2
        bOO=(max-min)/2
        if (min%2==0 and max%2==1) or (max%2==0 and min%2==1):
            nEO=random.randint (1,bEO)
            return (min+2*nEO)
        elif (min%2==0 and max%2==0):
            nEE=random.randint (1,bEE)
            return(min+2*nEE)
        else:
            nOO=random.randint (1,bOO)
            return (min+2*nOO-1)
