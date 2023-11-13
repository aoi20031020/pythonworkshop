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