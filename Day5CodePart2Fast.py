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


Lseeds=len(seeds)//2 
kseeds=0

for i in range(len(biglist)):
    while kseeds<Lseeds:
        for j in range(len(biglist[i])):
            if seeds[2*kseeds]>=biglist[i][j][1]+biglist[i][j][2] or seeds[2*kseeds]+seeds[2*kseeds+1]<=biglist[i][j][1]:
                #map and seed range are disjoint
                continue
            elif seeds[2*kseeds]<biglist[i][j][1] and seeds[2*kseeds]+seeds[2*kseeds+1]>biglist[i][j][1]+biglist[i][j][2]:
                #map is contained in seed range
                seeds.extend([seeds[2*kseeds],biglist[i][j][1]-seeds[2*kseeds]]) #add left part to the end
                seeds.extend([biglist[i][j][1]+biglist[i][j][2],seeds[2*kseeds]+seeds[2*kseeds+1]-biglist[i][j][1]+biglist[i][j][2]]) #add right part to the end
                seeds[2*kseeds]=biglist[i][j][0] #propagate middle part
                seeds[2*kseeds+1]=biglist[i][j][2]
                Lseeds+=2 #we added 2 seeds
                break
            elif seeds[2*kseeds]<biglist[i][j][1]:
                #split list into two parts and propagate until b
                seeds.extend([seeds[2*kseeds],biglist[i][j][1]-seeds[2*kseeds]]) #add left part to the end
                seeds[2*kseeds+1]-=biglist[i][j][1]-seeds[2*kseeds]
                seeds[2*kseeds]=biglist[i][j][0] #propagate middle part
                Lseeds+=1
                break

            elif seeds[2*kseeds]+seeds[2*kseeds+1]>biglist[i][j][1]+biglist[i][j][2]:
                #split list into two parts and propagate until a
                seeds.extend([biglist[i][j][1]+biglist[i][j][2],seeds[2*kseeds]+seeds[2*kseeds+1]-biglist[i][j][1]-biglist[i][j][2]])
                seeds[2*kseeds+1]=biglist[i][j][1]+biglist[i][j][2]-seeds[2*kseeds]
                seeds[2*kseeds]=biglist[i][j][0]+seeds[2*kseeds]-biglist[i][j][1]
                Lseeds+=1
                break
            elif seeds[2*kseeds]>=biglist[i][j][1] and seeds[2*kseeds]+seeds[2*kseeds+1]<=biglist[i][j][1]+biglist[i][j][2]:
               #seeds are contained in one map
                seeds[2*kseeds]=biglist[i][j][0]+seeds[2*kseeds]-biglist[i][j][1]
                break
        kseeds+=1
    kseeds=0
print(min([seeds[2*i] for i in range(len(seeds)//2)]))
