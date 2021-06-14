def func2(number):
    Temp = ''
    intnumber= 0
    for i in number:
        if i != '.':
            Temp += i
    Helpchange = len(Temp) - 1
    Help = ['0','1','2','3','4','5','6','7','8','9']
    
    for x in Temp:
        intnumber = intnumber + (Help.index(x) * (10 ** (Helpchange)))
        Helpchange -= 1
    return intnumber
