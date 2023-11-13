import random
def list_gen():
    list = []
    for n in range(100):
        list.append(n+1)
    random.shuffle(list)
    return list
