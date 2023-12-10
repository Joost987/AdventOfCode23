import re

def Propagate(pos,previousstep):
    (i,j)=previousstep

    if (i,j)==symboldict[gridlist[pos[0]][pos[1]]][0]:

        nextstep=(symboldict[gridlist[pos[0]][pos[1]]][1][0],symboldict[gridlist[pos[0]][pos[1]]][1][1])

    elif (-i,-j)==symboldict[gridlist[pos[0]][pos[1]]][1]:

        nextstep=(-symboldict[gridlist[pos[0]][pos[1]]][0][0],-symboldict[gridlist[pos[0]][pos[1]]][0][1])
        
    else:
        return pos, (0,0)
    pos=(pos[0]+nextstep[0],pos[1]+nextstep[1])
    return pos,nextstep

f=open("Day10Input.txt",'r')
gridlist=[]
symboldict={"|":((1,0),(1,0)),"-":((0,1),(0,1)),"L": ((0,-1),(-1,0)),"J":((0,1),(-1,0)),"7":((0,1),(1,0)),"F":((0,-1),(1,0))}

for (i,line) in enumerate(f):
    gridlist.append(line[:-1])
    if re.findall("S",line)!=[]: #this line seems pretty unnecessary, but might help with computation time?
        for (j,char) in enumerate(line):
            if char=="S":
                startpos=(i,j)
pos=startpos
nextstep=()
stepcount=0

for (i,j) in [(1,0),(0,1),(-1,0),(0,-1)]:
    if gridlist[startpos[0]+i][startpos[1]+j] in symboldict.keys():
        pos,step=Propagate((startpos[0]+i,startpos[1]+j),(i,j))
        if pos!=(startpos[0]+i,startpos[1]+j):
            stepcount+=2
            break

while True:
    pos,step=Propagate(pos,step)
    stepcount+=1
    if gridlist[pos[0]][pos[1]]=="S":
        break
print((stepcount+1)//2)
            