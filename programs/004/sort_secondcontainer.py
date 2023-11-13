import list_gen
import select
list = list_gen.list_gen()
secondlist = []
for i in range(10):
    count = []
    for n in range(10):
        count.append(list[(i * 10) + n])
    secondlist.append(count)
#パターン１
for i in range(10):
   secondlist[i] = select.select_sort(secondlist[i])
print(secondlist)

#パターン２
for i in range(10):
   secondlist[i] = select.select_sort(secondlist[i])
for Vindex in range(0, len(secondlist)):
    for Hindex in range(0,len(secondlist[Vindex])):
        Vmin, Hmin  = Vindex, Hindex
        for i in range(Vindex, len(secondlist)):
            if i == Vindex:
                for n in range(Hindex + 1, len(secondlist[Vindex])):
                    if secondlist[Vmin][Hmin] > secondlist[i][n]:
                        Vmin, Hmin = i, n
            else :
                for n in range(0, len(secondlist[Vindex])):
                    if secondlist[Vmin][Hmin] > secondlist[i][n]:
                        Vmin, Hmin = i, n
        secondlist[Vindex][Hindex], secondlist[Vmin][Hmin] = secondlist[Vmin][Hmin], secondlist[Vindex][Hindex]
print(secondlist)
        
