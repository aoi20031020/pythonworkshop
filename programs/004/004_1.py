list = []
list2 = 'Hello'
for i in range(5):
    list.append(input("何か入力"))
print(list)

for i in range(5):
    list.insert(i*2, i)
print(list)

list.extend(list2)
print(list)