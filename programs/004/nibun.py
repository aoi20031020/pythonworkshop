import list_gen2

list = list_gen2.list_gen()
list.sort()
num = int(input("what num?"))
lo = 0
hi = len(list) - 1
mid = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if list[mid] == num:
        print("{}は{}番目にあります".format(num, mid + 1))
        exit()
    elif list[mid] < num:
        lo = mid + 1
    else:
        hi = mid - 1
print("要素にない数です")