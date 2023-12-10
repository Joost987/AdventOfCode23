#note: This code is quite slow, my input took 2.5 minutes to compute. To make it faster you can do the following:
#When checking the crossings of a point (i,j) and another point that is not on the curve is found,
#then if the current amount of crossings is even, this new point is interior iff (i,j) is interior
#and if the current amount of crossings is uneven, the new point will not be interior iff (i,j) is interior.
#Hence one should keep track of all the points that are found during CheckCrossings that are not on the point
#and if the amount of crossings to get there is even or odd. Then CheckCrossings can return a list of
#interior points and a list of exterior points, then do not need to be checked anymore. 
#I think with this approach only one point for each i and one point for each j needs to be checked,
#so for a square grid only 2*i points. This should reduce time complexity from O(n^2) to O(n)

import re

def Propagate(pos,previousstep): #This function takes the next step onto our curve
    (i,j)=previousstep

    if (i,j)==symboldict[gridlist[pos[0]][pos[1]]][0]:
        nextstep=(symboldict[gridlist[pos[0]][pos[1]]][1][0],symboldict[gridlist[pos[0]][pos[1]]][1][1])

    elif (-i,-j)==symboldict[gridlist[pos[0]][pos[1]]][1]:
        nextstep=(-symboldict[gridlist[pos[0]][pos[1]]][0][0],-symboldict[gridlist[pos[0]][pos[1]]][0][1])
        
    else:
        return pos, (0,0)
    pos=(pos[0]+nextstep[0],pos[1]+nextstep[1])
    return pos,nextstep

def CheckCrossings(pos,direction,curve): #This function checks how many crossings there are for a certain point and direction
    (i,j)=pos
    (l,m)=direction
    k=1
    crossings=0
    enteringsymb=""
    while 0<=i+k*l<=len(gridlist) and 0<=j+k*m<=len(gridlist[0]):
        if (i+k*l,j+k*m) in curve:
            if enteringsymb=="" and gridlist[i+k*l][j+k*m] in iddict.keys():
                enteringsymb=gridlist[i+k*l][j+k*m]
            elif enteringsymb!="" and gridlist[i+k*l][j+k*m] in iddict.keys():
                    if gridlist[i+k*l][j+k*m] in iddict[enteringsymb]:
                        crossings+=2
                    else:
                        crossings+=1
                    enteringsymb=""

            elif enteringsymb=="" and l==0 and gridlist[i+k*l][j+k*m]=="|":
                crossings+=1
                k+=1
                continue
            elif enteringsymb=="" and m==0 and gridlist[i+k*l][j+k*m]=="-":
                crossings+=1
                k+=1
                continue     
        k+=1
    return crossings
                

#The first dictionary translates the symbols into directions
symboldict={"|":((1,0),(1,0)),"-":((0,1),(0,1)),"L": ((0,-1),(-1,0)),"J":((0,1),(-1,0)),"7":((0,1),(1,0)),"F":((0,-1),(1,0))}

#This dictionary shows which combination leads to a double crossing, for example if we encounter F--7, this should be adouble crossing as 7 is in iddict["F"]
iddict={"F":["L","7"],"L":["F","J"],"7":["J","F"],"J":["7","L"]}

#This dictionary is for replacing S with the symbol it should exactly be
replaceSdict={((1,0),(-1,0)):"|",((0,1),(0,-1)):"-",((0,1),(-1,0)):"L",((0,-1),(1,0)):"J",((0,-1),(1,0)):"7" ,((0,1),(1,0)):"F", ((-1,0),(1,0)):"|",((0,-1),(0,1)):"-",((-1,0),(0,1)):"L",((1,0),(0,-1)):"J",((1,0),(0,-1)):"7" ,((1,0),(0,1)):"F"  }


f=open("Day10Input.txt",'r')
gridlist=[]

for (i,line) in enumerate(f): #In this part we put all the lines into a list and find S

    gridlist.append(line[:-1])
    if re.findall("S",line)!=[]: #this line seems pretty unnecessary, but might help with computation time?
        for (j,char) in enumerate(line):
            if char=="S":
                startpos=(i,j)

gridlist[-1]=line

pos=startpos
nextstep=()
curve=[startpos]
SRealLetter=[]

for (i,j) in [(1,0),(0,1),(-1,0),(0,-1)]: #In this part we find out what symbol S should be, and what the next 2 steps are
    if gridlist[startpos[0]+i][startpos[1]+j] in symboldict.keys():
        pos,step=Propagate((startpos[0]+i,startpos[1]+j),(i,j))

        if pos!=(startpos[0]+i,startpos[1]+j) and len(SRealLetter)==1:
            curve.append((startpos[0]+i,startpos[1]+j))
            curve.append(pos)
            SRealLetter.append((i,j))

            temp=list(gridlist[startpos[0]])
            temp[startpos[1]]=replaceSdict[tuple(SRealLetter)]#key
            gridlist[startpos[0]]="".join(temp)
            break
        elif pos!=(startpos[0]+i,startpos[1]+j) and SRealLetter==[]:
            SRealLetter.append((i,j))

while True: #iterate until we are back at the starting position and add the points to our curve
    pos,step=Propagate(pos,step)
    curve.append(pos)
    if pos==startpos:
        break

som=0
print("calculated curve")
for i in range(len(gridlist)):
    for j in range(len(gridlist[0])):
        if not (i,j) in curve:
            interior=True
            for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
                if CheckCrossings((i,j),direction,curve)%2==0:
                    interior=False
                    #temp=list(gridlist[i]) #replaces exterior points with .
                    #temp[j]="."
                   #gridlist[i]="".join(temp)
                    break
            som+=interior
            #if interior:
                   # temp=list(gridlist[i]) #replaces interior points with 0
                   # temp[j]="0"
                    #gridlist[i]="".join(temp)
print(som)
print(len(curve))
