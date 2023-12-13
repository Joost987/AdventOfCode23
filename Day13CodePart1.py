def CheckColumnSymmetries(mediumlst):
    possiblesymmetries=list(range(1,len(mediumlst[0])))
    for i in range(len(mediumlst)):
        possiblesymmetriescopy=possiblesymmetries.copy()
        for symmetry in possiblesymmetries:
            for j in range(1,min(len(mediumlst[0])-symmetry,symmetry)+1):
                #print(len(mediumlst[i]),symmetry,j)
                if mediumlst[i][symmetry-j]!=mediumlst[i][symmetry-1+j]:
                    possiblesymmetriescopy.remove(symmetry)
                    break
        possiblesymmetries=possiblesymmetriescopy
    return possiblesymmetries

def CheckRowSymmetries(mediumlst):
    possiblesymmetries=list(range(1,len(mediumlst)))
    for j in range(len(mediumlst[0])):
        possiblesymmetriescopy=possiblesymmetries.copy()
        for symmetry in possiblesymmetries:
            for i in range(1,min(len(mediumlst)-symmetry,symmetry)+1):
                if mediumlst[symmetry-i][j]!=mediumlst[symmetry-1+i][j]:
                    possiblesymmetriescopy.remove(symmetry)
                    break
        possiblesymmetries=possiblesymmetriescopy
    return possiblesymmetries

f=open("Day13Input.txt","r")
chunks=f.read().split("\n\n")
som=0
for chunk in chunks:
    mediumlst=chunk.split("\n")
    if mediumlst[-1]=="":
        mediumlst=mediumlst[:-1]
    som+=sum(CheckColumnSymmetries(mediumlst))+100*(sum(CheckRowSymmetries(mediumlst)))
print(som)
