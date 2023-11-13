list = [1,2,3,4,5,6,7,8,9,1]
print(list)
del list[2]
print(list)
list.pop(3)
print(list)
#配列に同じ値がある場合最初の要素のみ削除
list.remove(1)
print(list)