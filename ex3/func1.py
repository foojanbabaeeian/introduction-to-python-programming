def func1(Sentence):
    Sp=[]
    temp = ''
    for i in Sentence:
        if i == ' ':
            Sp.append(temp)
            temp=''
        else:
            temp=temp+i
    if temp:
        Sp.append(temp)
    return Sp
