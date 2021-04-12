import random
#E stands for EVEN numbers
#O stands for ODD numbers
#ex :::> bEO is the amount of even numbers between an even and odd number
def Rand2(num1,num2):
    '''int :::> int
this function gets two numbers and gives an even number randomly between them'''
    bEO=(num2-(num1+1))/2
    bEE=(num2-num1-2)/2
    bOO=(num2-num1)/2
    start=1
    if (num1%2==0 and num2%2==1) or (num2%2==0 and num1%2==1):
        nEO=random.randint (1,bEO)
        print (num1+2*nEO)
    elif (num1%2==0 and num2%2==0):
        nEE=random.randint (1,bEE)
        print(num1+2*nEE)
    else:
        nOO=random.randint (1,bOO)
        print (num1+2*nOO-1)
