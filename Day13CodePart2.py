def CheckColumnSymmetries(mediumlst):
    possiblesymmetries=list(range(1,len(mediumlst[0])))
    for i in range(len(mediumlst)):
        possiblesymmetriescopy=possiblesymmetries.copy()
        for symmetry in possiblesymmetries:
            for j in range(1,min(len(mediumlst[0])-symmetry,symmetry)+1):
                if mediumlst[i][symmetry-j]!=mediumlst[i][symmetry-1+j]:
                    possiblesymmetriescopy.remove(symmetry)
                    break
        possiblesymmetries=possiblesymmetriescopy
    return possiblesymmetries

def CheckColumnSmudgedSymmetries(mediumlst):
    possiblesymmetries=list(range(1,len(mediumlst[0])))
    smudgedict={}
    for i in range(len(mediumlst)):
        possiblesymmetriescopy=possiblesymmetries.copy()
        for symmetry in possiblesymmetries:
            for j in range(1,min(len(mediumlst[0])-symmetry,symmetry)+1):
 
                if mediumlst[i][symmetry-j]!=mediumlst[i][symmetry-1+j]:
                    if symmetry in smudgedict.keys():
                        possiblesymmetriescopy.remove(symmetry)
                        del smudgedict[symmetry]
                        break
                    else:
                        smudgedict.update({symmetry:[i,j,symmetry]})
        possiblesymmetries=possiblesymmetriescopy
    for symmetry in possiblesymmetriescopy:
        if symmetry not in smudgedict.keys():
            possiblesymmetries.remove(symmetry)
    if len(smudgedict.values())==0:
        return 0
    if len(smudgedict.values())==1:
        oldSymmetries=set(CheckRowSymmetries(mediumlst))
        smudge=smudgedict[possiblesymmetries[0]]
        lst=list(mediumlst[smudge[0]])
        lst[smudge[2]-smudge[1]]=lst[smudge[2]-1+smudge[1]]
        mediumlst[smudge[0]]="".join(lst)
        return sum(list(smudgedict.keys()))+100*sum(set(CheckRowSymmetries(mediumlst))-oldSymmetries)


    if len(smudgedict.values())>1:
        print(smudgedict)
        raise(RuntimeError)
        return None
    

def CheckRowSmudgedSymmetries(mediumlst):
    possiblesymmetries=list(range(1,len(mediumlst)))
    smudgedict={}
    for j in range(len(mediumlst[0])):
        possiblesymmetriescopy=possiblesymmetries.copy()
        for symmetry in possiblesymmetries:
            for i in range(1,min(len(mediumlst)-symmetry,symmetry)+1):
                if mediumlst[symmetry-i][j]!=mediumlst[symmetry-1+i][j]:
                    if symmetry in smudgedict.keys():
                        possiblesymmetriescopy.remove(symmetry)
                        del smudgedict[symmetry]
                        break
                    else:
                        smudgedict.update({symmetry:[i,j,symmetry]})
        possiblesymmetries=possiblesymmetriescopy
    for symmetry in possiblesymmetriescopy:
        if symmetry not in smudgedict.keys():
            possiblesymmetries.remove(symmetry)
    if len(smudgedict.values())==0:
        return 0
    elif len(smudgedict.values())==1:
        oldSymmetries=set(CheckColumnSymmetries(mediumlst))
        #print(smudgedict,possiblesymmetries)
        smudge=smudgedict[possiblesymmetries[0]]

        lst=list(mediumlst[smudge[2]-smudge[0]])
        #print(len(mediumlst),len(lst),lst,smudge)
        lst[smudge[1]]=mediumlst[smudge[2]-1+smudge[0]][smudge[1]]
        mediumlst[smudge[2]-smudge[0]]="".join(lst)
        
        return 100*sum(list(smudgedict.keys()))+sum(set(CheckColumnSymmetries(mediumlst))-oldSymmetries)


    elif len(smudgedict.values())>1:
        print(smudgedict)
        raise(RuntimeError)
        return None

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
    som+=CheckColumnSmudgedSymmetries(mediumlst)+CheckRowSmudgedSymmetries(mediumlst)

print(som)
