f=open("Day9Input.txt",'r')

som=0

for line in f:
    biglist=[]
    toplist=line.split(" ")
    toplist=[int(i) for i in toplist]
    j=0
    biglist.append(toplist)
    while biglist[j]!=[0]*len(biglist[j]):
        newlist=[biglist[j][k]-biglist[j][k-1] for k in range(1,len(biglist[j]))]
        biglist.append(newlist)
        j+=1
    biglist[j].append(0)
    for k in range(2,len(biglist)):
        biglist[len(biglist)-k].append(biglist[len(biglist)-k][-1]+biglist[len(biglist)-k+1][-1])
    som+=biglist[0][-1]+biglist[1][-1]


print(som)