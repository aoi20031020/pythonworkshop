import list_gen
list = list_gen.list_gen()
length = len(list)
for index in range(1, length):
    arrange = list[index]
    prev = index - 1
    while prev >= 0 and list[prev] > arrange:
        list[prev + 1] = list[prev]
        prev = prev - 1
    list[prev + 1] = arrange
print(list)