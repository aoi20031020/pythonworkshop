import list_gen
list = list_gen.list_gen()
length = len(list)
for index in range(0,length - 1):
    min = index
    for n in range(index + 1, length):
        if list[min] > list[n]:
            min = n
    list[index], list[min] = list[min], list[index]

#print(list)
def select_sort(list):
    length = len(list)
    for index in range(0,length - 1):
        min = index
        for n in range(index + 1, length):
            if list[min] > list[n]:
                min = n
        list[index], list[min] = list[min], list[index]
    return(list)
