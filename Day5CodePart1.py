import re
f=open("Day5Input.txt",'r')
firstline=f.readline()
f.readline()
f.readline()
seeds=re.findall("\s\d+",firstline)
seeds=[int(i) for i in seeds]
biglist=[]
mediumlst=[]
for line in f:
    line=" "+line
    numbers=re.findall("\s\d+",line)
    if numbers!=[]:
        numbers=[int(i) for i in numbers]
        mediumlst.append(numbers)
    else:
        biglist.append(mediumlst)
        mediumlst=[]
        f.readline()
biglist.append(mediumlst)
mediumlst=[]

for i in range(len(biglist)):
    for k in range(len(seeds)):
        for j in range(len(biglist[i])):
            if seeds[k] in range(biglist[i][j][1],biglist[i][j][1]+biglist[i][j][2]):
                seeds[k]-=biglist[i][j][1]-biglist[i][j][0]
                break
                
#print(seeds)
print(min(seeds))