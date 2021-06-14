def func3(num):
    count = 1
    cutnum = 0
    while num > count:
        count = count * 10
    while num > 1:
        while num > count:  
            cutnum += count          
            num=num- count
        count = count // 10
    return cutnum
