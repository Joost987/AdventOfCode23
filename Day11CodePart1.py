def Dist(galaxy,galaxyother,expansiondistance=1):
    temp=galaxy
    galaxy=(max(galaxy[0],galaxyother[0]),max(galaxy[1],galaxyother[1]))
    galaxyother=(min(temp[0],galaxyother[0]),min(temp[1],galaxyother[1]))
    distance=galaxy[0]-galaxyother[0]+galaxy[1]-galaxyother[1]
    for i in range(galaxyother[0],galaxy[0]):
        if i in rowsexpanded:
            distance+=expansiondistance
    for j in range(galaxyother[1],galaxy[1]):
        if j in columnsexpanded:
            distance+=expansiondistance
    return distance

f=open("Day11Input.txt",'r')

galaxylist=[]
rowsexpanded=[]
maxi=0
for (i,line) in enumerate(f):
    foundgalaxy=False
    for (j,char) in enumerate(line):
        if char=="#":
            galaxylist.append((i,j))
            foundgalaxy=True
            maxi=max(j,maxi)
    if not foundgalaxy:
        rowsexpanded.append(i)

galaxycols=[galaxy[1] for galaxy in galaxylist]
columnsexpanded=[]
for i in range(maxi+1):
    if i not in galaxycols:
        columnsexpanded.append(i)

som=0
for i in range(len(galaxylist)):
    for j in range(i+1,len(galaxylist)):
        som+=Dist(galaxylist[i],galaxylist[j],1000000-1) #change this to 2 for part 1
print(som)