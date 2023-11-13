import random

def has_duplicates(list):
        return len(list) != len(set(list))

def list_gen():
    list = []
    rand = random.randrange(1, 501)
    list.append(rand)
    n = 0 
    flg = 0

    while len(list) < 100:
        rand = random.randrange(1, 501)
        list.append(rand)
        flg = has_duplicates(list)
        if flg == True:
            list.pop(n + 1)
        else:
            n = n + 1
            
    return list



