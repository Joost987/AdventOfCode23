f=open("Day14Input.txt")

def SlideRocksNColumn(column):
    rockslst=[[]]
    cubelst=[-1]
    for i in range(len(column)):
        if column[i]=="#":
            cubelst.append(i)
            rockslst.append([])
        elif column[i]=="O":
            if rockslst[-1]!=[]:
                rockslst[-1].append(rockslst[-1][-1]+1)
            else:
                rockslst[-1].append(cubelst[-1]+1)
    rockslst=[rock for rocks in rockslst for rock in rocks]
    return rockslst


biglist=[]
for line in f:
    biglist.append(line.split("\n")[0])

som=0
for j in range(len(biglist[0])):
    columnj="".join([biglist[i][j] for i in range(len(biglist))])
    rocks=SlideRocksNColumn(columnj)
    som+=sum([len(biglist)-rock for rock in rocks])
print(som)
