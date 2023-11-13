import list_gen
list = list_gen.list_gen()
length = len(list)
for i in range(1, length):
        for j in range(0, length-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

print(list)