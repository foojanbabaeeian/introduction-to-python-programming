fruits = ['apple','banana','cherry']
for x in fruits:
	if x == 'banana':
		continue
	print(x)
	'''skips banana and prints [apple , cherry]'''
'''if you want to print them in one line you must use ---end=""--- in print
cause print is programmed to print them in different lines'''
print(x, end= ' ')
	**********************************************************
for x in range(3,10,2):
    print(x)
    '''jumps 2 by 2'''
else:
    print('End Loop')
    **************************************************************************
for x in range(3,10):
    if x==5:
        continue
    print(x)
else:
    print('End Loop')
    *****************************************************************
adj=['red','big','tasty']
fruits = ['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print (x,y)
        **************************************************************
        assignment::
            
for a in range (1,11):
    for b in range(1,11):
        print('{:4}'.format(a*b), end='')
    print('')
    *******************************************************************
LIST:
    mutable/
    .
    .
fruits=['apple','banana','cherry']
    print (fruits[:2])
    ''' prints apple, banana....if it was [-2:] it would print banana , cherry'''

*****************************************************************************        
fruits=['apple','banana','cherry']
fruits[1]='orange'
    print (fruits)
    '''it would replace banana with orange because list is mutable against tuple'''
********************************************************************************
fruits.append
fruits.insert(0,'orange')
***********************************************************************
DATA
    ONE VALUE:
        str
        int
        float
        bool
    MORE THAN ONE VALUE:
        arrey:
        list

        tuple

        dict
FUNCTION:(have been defined for more than one data types)
insert 
append
remove
sort=> sort(reverse= True)
'''will sort the numbers from the largest to the smallest'''
del
******************************************************************************
'''ascii is a system for numbers and letters with codes '''

TUPLE:
    unmutable(object does not support item assignment) /ordered
    / duplicate values (can contain two similar values)/str and nums are defined
******************************************************************************

#a is a list of numbers 
a= [5.5,'ali',9,1000]
print (a)
a.sort()
'''it doesn't sort the list because it must contain only one type ,
either str or int '''
a= [5.5,-1,9,1000]
print (a)
a.sort()
...............................
#b is a list of students names
b=['mina','hadi','ali',]
print('my list contains '/str' ')
b.sort()
print(b)
.............................
FUNCTION
*****************************************
a= [5.5,2,9,1000]
a.sort()
def FuncPrtList():
    print('my list is ')
    print (a)
b()
*************************
def FuncPowr(myNum):
        print('myNum : ',myNum)
        myNum *=myNum
        return myNum
x=7
print(FuncPowr(x))
y=9
print((FuncPowr(x))+(FuncPowr(y)))
************************************
def FuncPowr(myNum):
    FuncPrint(myNum)
    myNum *=myNum
    return myNum
'''return makes a new value each time
and returns it to the function
print only makes one value and prints it'''
def FuncPrint(x):
    print('myNum : ',x)
x=7
'''first code '''
y=9
x=(FuncPowr(x)+FuncPowr(y))
print ('x :  ' , FuncPowr(x))
y=FuncPrint(x)
FuncPrint(y)
'''FuncPrint function returns None at the end of it after print because it doesn't have return and y=None
when we call this function with value of y it prints:: myNum : None '''

**********************************************************************************************************
def Factorial(x):
    multiply=1
    for i in range (2,x+1):
        multiply *= i
    print ('Factorial' , x, 'is' ,multiply)
a=5
Factorial (a)
***************************************************************************************
def Factorial(x):
    multiply=1
    for i in range (2,x+1):
        multiply *= i
    return multiply
def printFunc(x):
    print ('Factorial' , x, 'is' ,Factorial(x))
a=5
printFunc(a)
*******************************************************
def Factorial(x):
    multiply=1
    for i in range (2,x+1):
        multiply *= i
    return multiply
def printFunc(x):
    print ('Factorial' , x, 'is' ,Factorial(x))
def recurvefactorial(k):
    result=1
    if (k>0):
        result= k * recurvefactorial(k-1)
    else:
        result=1
    return result
*******************************************************
LAMBDA FUNCTIONS:
        '''anonymous function and can be used only once'''
lambda x : x+5
myFunc = lambda x: x*4
..........................................
myFunc = lambda x:x*4
print (myFunc(5))
*********************
a=[(2,5),(4,3),(6,7),(1,9)]
print(a)

a.sort()
print(a)

a.sort(key = lambda x:x[1])
print(a)
********************************
x=lambda a :a+10
print(x(5))

def aname(x):
        return x+x
..............
k=lambda x:x+x
k= lambda x,y:x+y
print(k(9,5))

*********************
def myFunc(n):
        return lambda a:a*n
mydoubler=myFunc(2)
print (mydoubler(11))
*********************
def myFunc():
    return lambda a:a/2
x=myFunc()
print(x(11))
***********************************
first=[12.5,15,14,16,14.75]
second=list(map(lambda a:a+2,first ))
print (second)
********************************
resultlist=list(map(lambda a:a**2,[5,12,8] ))
print (resultlist)
**********************************************
def power(n):
        return n*n
print(list(map(power, [3,5,8,7])))
*****************************************
FILTER FUNCTION:
'''we can filter the function and get what we need'''
*********************************************************
names=['fozhan','hannane','hadi','mina','boo']
nameslast=list(filter(lambda x:len(x)<=4,names))
print(nameslast)
print(names)
**************************************************************
def myFunc():
    filterlist= list(filter(lambda x:x>=50,[10,50,70]))
    return filterlist
print (myFunc())
********************************************************
myList=[-5,0,5,9,-8]
rslt=list(map(lambda x:'negative' if x<0 else 'positive',myList))
print(myList)
print(rslt)
**************************************************************
def v(a):
    return a*2
print(v(10))
****************
def listfunc(list1):
    return list(map(lambda x:x*2,list1))
print (listfunc([2,4,8]))
***********************************************
import functools
mylist=[1,3,5,7,9]
print(functools.reduce(lambda a,b: a+b , mylist))
***************************************************
import functools
termgrade = [10,11,12]
print (functools.reduce(lambda a,b: a+b , termgrade))
..........................................................
import functools
def avgclass(termgrade):
        ave=((functools.reduce(lambda a,b: a+b , termgrade))/len(termgrade)
        return ave
print ('my class average is' avgclass(termgrade))
*************************************************************************
def func(a):
        for i in range (1,a+1):
                print(i)
print (func(10))
       ******************
def num(a):
    while a<5:
        print (a)
        a=a+1

***********************
def mygenfunc(n):
        num=0
        while (num<n):
                yield num
                num +=1
for i in mygenfunc(10):
        print(i)
************************************************
def myFunc(a):
        print('in function',end= ' ')
        return a*a
print('enter your name:')
x=input()
print('hello,'+x)
print(type(x))
print('enter a number')
x=input()
print(type(x))
x=8
print(type(x))
print(myFunc(x))
print('end of program.')
*******************************
def generator():
        count=1
        print('in function: ', count)
        yield 1
        count+=1
        print('in function: ', count)
        yield 2
        count+=1
        print('in function: ', count)
        yield 3
print('start program')
for value in generator():
        print('in main part:')
        print(value)
*********************************************
def generator():
        yield 1
        yield 2
        yield 3
x= generator()
print(type(x))
.......................
def generator(n):
        num=0
        while(num<n):
                yield num
                num+=1
for i in generator(10):
        print(i)
.............................................
def Course():
    x=input('enter course name: ')
    garde= input('please enter your grade:')
    return grade
ave=0
for i in range(1,4):
    ave=ave+ int(Course())
print('sum of grade', ave/3)

**********************************************8
OBJECT ORIENTED Programming in python
#class
.object
.variable
.method
.override
.class variable
..................
        
