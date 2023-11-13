i = 0
p = 1
#複数条件や否定でもOK
while not((i+p)%7 == 0):
    print("{}回目".format(i+1))
    i = i + 1
    p = i + p  