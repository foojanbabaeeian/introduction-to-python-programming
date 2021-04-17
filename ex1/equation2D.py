def equation2D (a,b,c):
    '''int :::> float
this function gets a,b,c of a quadratic equation formula , and calculates the roots . if there is none :::> none ,and if there is one :::> x1=x2=the number'''
    delta=(b**2)-(4*a*c)
    x1=(-b+(delta**0.5))/2*a
    x2=(-b-(delta**0.5))/2*a
    if delta==0:
        return ('x1=x2={}'.format(x1))
    elif delta>0:
        return ('x1={} and x2={}'.format(x1,x2))
    else:
        return ('none')
