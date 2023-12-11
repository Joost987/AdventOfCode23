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

def CheckCrossingsList(pos,direction,curve): #This function checks how many crossings there are for a certain point and direction
    (i,j)=pos
    (l,m)=direction
    k=1
    crossings=0
    enteringsymb=""
    SameAsPos=[pos]
    notSameAsPos=[]
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
        else:
            if crossings%2==0:
                SameAsPos.append((i+k*l,j+k*m)) 
            else:
                 notSameAsPos.append((i+k*l,j+k*m))  
        k+=1
    if crossings%2==0:
        return SameAsPos,notSameAsPos
    else:
        return notSameAsPos,SameAsPos

                

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
for j in range(len(gridlist)):
    som+=len(CheckCrossingsList((0,j),(1,0),curve)[1])

print(som)

print(len(curve))
