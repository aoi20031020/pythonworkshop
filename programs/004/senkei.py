import list_gen #次回解説します
list = list_gen.list_gen() #ランダムなリストを取得
num = int(input("what number?"))
n = 0
while not(num == list[n]):
    n = n + 1
    if n == len(list):
        print("その数は要素に含まれてないです")
        exit()
print(list)
print("{}は{}番目にありました".format(num, n))
