f=open("Day14Input.txt")

def SlideRocksNColumn(column):
    rockslst=[[]]
    cubelst=[-1]
    for i in range(len(column)):
        if column[i]=="#":
            cubelst.append(i)
            rockslst.append([])
        elif column[i]=="O":
            if rockslst[-1]!=[]:
                column[i]="."
                column[rockslst[-1][-1]+1]="O" #note that keeping the rocklist is not needed, might want to delete if slow
                rockslst[-1].append(rockslst[-1][-1]+1)
            else:
                column[i]="."
                column[cubelst[-1]+1]="O"
                rockslst[-1].append(cubelst[-1]+1)

    return column

def TransposeAndSlide(biglist):
    newbiglisttransposed=[]
    for j in range(len(biglist[0])):
        columnj=[biglist[i][j] for i in range(len(biglist))]
        columnj=SlideRocksNColumn(columnj)
        newbiglisttransposed.append(columnj)
    return newbiglisttransposed

def Cycle(biglist):
    #slide north and east
    biglist=TransposeAndSlide(TransposeAndSlide(biglist))
    #reverse biglist
    biglist=[[biglist[len(biglist)-1-i][j] for j in range(len(biglist[0]))] for i in range(len(biglist))]
    #slide south
    biglist=TransposeAndSlide(biglist)
    #reverse biglist
    biglist=[[biglist[len(biglist)-1-i][j] for j in range(len(biglist[0]))] for i in range(len(biglist))]
    #slide west
    biglist=TransposeAndSlide(biglist)
    #mirror
    biglist=[[biglist[len(biglist)-1-i][len(biglist[0])-1-j] for j in range(len(biglist[0]))] for i in range(len(biglist))]
    return biglist

def CalculateLoad(biglist):
    som=0
    for j in range(len(biglist[0])):
        for i in range(len(biglist)):
            if biglist[i][j]=="O":
                som+=len(biglist)-i
    return som

biglist=[]
for line in f:
    biglist.append(line.split("\n")[0])


loadlst=[]
initrun=0 #use this to filter out any part until the cycles begin.
findperiodrun=1000
for i in range(initrun):
    biglist=Cycle(biglist)
for i in range(findperiodrun):


        
    biglistnew=Cycle(biglist)
    load=CalculateLoad(biglist)
    if loadlst.count(load)==3:
        indexes=[j for j in range(len(loadlst)) if loadlst[j]==load]
        if indexes[1]-indexes[0]==indexes[2]-indexes[1]: 
            cyclelen=indexes[1]-indexes[0]
            endpos=(1000000000-initrun-indexes[0])%(indexes[1]-indexes[0])
            print(loadlst[indexes[0]+endpos],indexes[0]+endpos+initrun)
            break
    loadlst.append(load)

    biglist=biglistnew

