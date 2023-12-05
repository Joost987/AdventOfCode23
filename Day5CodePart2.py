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

startlocation=10000000
Lbig=len(biglist)-1
breakpar=False
while startlocation<=14400000:
    location=startlocation
    for i in range(len(biglist)):
            for j in range(len(biglist[Lbig-i])):
                if location in range(biglist[Lbig-i][j][0],biglist[Lbig-i][j][0]+biglist[Lbig-i][j][2]):
                    location+=biglist[Lbig-i][j][1]-biglist[Lbig-i][j][0]
                    break
    for k in range(len(seeds)//2):
        if location in range(seeds[2*k],seeds[2*k]+seeds[2*k+1]):
            print("\n",location,seeds[2*k],seeds[2*k]+seeds[2*k+1])
            breakpar=True
            break
    if breakpar:
        break
    startlocation+=1.



print(startlocation, location)