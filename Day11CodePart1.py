
def Dist(galaxy ,  galaxyother):
    temp  =  galaxy
    galaxy = (max(galaxy[0] , galaxyother[0]) , max(galaxy[1] , galaxyother[1]))
    galaxyother = (min(temp[0] , galaxyother[0]) , min(temp[1] , galaxyother[1]))
    distance = galaxy[0]-galaxyother[0] +galaxy[1]-galaxyother[1]

    return distance



def ExpandGalaxy(galaxy , expansiondistance = 1):
    for i in range(galaxy[0]):
        if i in rowsexpanded:
            galaxy = (galaxy[0] +expansiondistance , galaxy[1])
    for j in range(galaxy[1]):
        if j in columnsexpanded:
            galaxy = (galaxy[0] , galaxy[1] +expansiondistance)
    return galaxy

f = open("Day11Input.txt" , 'r')

galaxylist = []
rowsexpanded = []
maxi = 0
for (i , line) in enumerate(f):
    foundgalaxy = False
    for (j , char) in enumerate(line):
        if char == "#":
            galaxylist.append((i , j))
            foundgalaxy = True
            maxi = max(j , maxi)
    if not foundgalaxy:
        rowsexpanded.append(i)



galaxycols = [galaxy[1] for galaxy in galaxylist]
columnsexpanded = []
for i in range(maxi +1):
    if i not in galaxycols:
        columnsexpanded.append(i)

galaxylist = [ExpandGalaxy(galaxy , expansiondistance = 1000000-1) for galaxy in galaxylist] #change this to 1 for part 1
som = 0
for i in range(len(galaxylist)):
    for j in range(i +1 , len(galaxylist)):
        som += Dist(galaxylist[i] , galaxylist[j]) 
print(som)