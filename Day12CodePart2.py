
def Function(number,symbollist):
    possiblestarts=[]
    FoundLatest=False
    latest=len(symbollist)
    for i in range(len(symbollist)-number):
        startloc=True
        for j in range(i,i+number):
            if symbollist[j]==".":
                startloc=False
                break
            if symbollist[j]=="#" and not FoundLatest:
                FoundLatest=True
                latest=j

        if startloc and symbollist[i+number]!="#":
            possiblestarts.append(i)
        if FoundLatest and i==latest:
            break
    return possiblestarts




f=open("Day12Input.txt", 'r')
bigsymbollist=[]
bignumberlist=[]
for line in f:
    symbs,numbers=line.split(" ")
    numbers=numbers.split(",")
    numbers=[int(number) for number in numbers]
    bignumberlist.append(numbers*5)
    bigsymbollist.append(list(symbs)+(["?"]+list(symbs))*4+["."]*bignumberlist[-1][-1])


som=0

for i in range(len(bigsymbollist)):
    posArrangementLastdict={}

    for j in range(len(bignumberlist[i])):

        lateststart=len(bigsymbollist[i])-sum([number+1 for number in bignumberlist[i][j:]])+1
        if posArrangementLastdict=={}:
                
                possiblestarts=Function(bignumberlist[i][j],bigsymbollist[i][:lateststart+1+bignumberlist[i][j]])
                for start in possiblestarts:

                    posArrangementLastdict.update({start:1})
        else:

            posArrangementLastdictNew={}

            for lastinarr in posArrangementLastdict.keys():

                earlieststart=lastinarr+bignumberlist[i][j-1]+1
                possiblestarts=Function(bignumberlist[i][j],bigsymbollist[i][earlieststart:lateststart+1+bignumberlist[i][j]])
                possiblestarts=[start+earlieststart for start in possiblestarts]

                for start in possiblestarts:
                    if start in posArrangementLastdictNew.keys():

                        posArrangementLastdictNew.update({start:posArrangementLastdictNew[start]+posArrangementLastdict[lastinarr]})
                    
                    else:
                        posArrangementLastdictNew.update({start:posArrangementLastdict[lastinarr]})

            posArrangementLastdict=posArrangementLastdictNew
            
    posArrangementLastdictNew=posArrangementLastdict.copy()
    for lastinarr in posArrangementLastdict:
        if "#" in bigsymbollist[i][lastinarr+bignumberlist[i][-1]:]:
            del posArrangementLastdictNew[lastinarr]
    posArrangementLastdict=posArrangementLastdictNew
    #print(sum(list(posArrangementLastdict.values())))
    som+=sum(list(posArrangementLastdict.values()))



print(som)