f=open("Day12Input.txt", 'r')

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

bigsymbollist=[]
bignumberlist=[]
for line in f:
    symbs,numbers=line.split(" ")
    numbers=numbers.split(",")
    numbers=[int(number) for number in numbers]
    bignumberlist.append(numbers)
    bigsymbollist.append(list(symbs)+["."]*bignumberlist[-1][-1]) #very inefficient solution

som=0

for i in range(len(bigsymbollist)):
    posArrangement=[]

    for j in range(len(bignumberlist[i])):
        lateststart=len(bigsymbollist[i])-sum([number+1 for number in bignumberlist[i][j:]])+1
        if posArrangement==[]:
                possiblestarts=Function(bignumberlist[i][j],bigsymbollist[i][:lateststart+1+bignumberlist[i][j]])
                posArrangement.extend([[start] for start in possiblestarts])
        else:
            posArrangementNew=posArrangement.copy()
            for arr in posArrangement:
                
                earlieststart=arr[-1]+bignumberlist[i][j-1]+1
                possiblestarts=Function(bignumberlist[i][j],bigsymbollist[i][earlieststart:lateststart+1+bignumberlist[i][j]])
                possiblestarts=[start+earlieststart for start in possiblestarts]
                posArrangementNew.extend([arr+[start] for start in possiblestarts])
                posArrangementNew.remove(arr)
            posArrangement=posArrangementNew

    posArrangementNew=posArrangement.copy()
    for arr in posArrangement:
        if "#" in bigsymbollist[i][arr[-1]+bignumberlist[i][-1]:]:
            posArrangementNew.remove(arr)
    posArrangement=posArrangementNew
    som+=len(posArrangement)
    #print(len(posArrangement))

print(som)