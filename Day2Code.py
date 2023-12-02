def CheckCol(linelst,num):
    for b in linelst:
        try:
            if int(b[-3:-1])>num:
                return True
        except:
            continue
    return False

def GetMax(linelst):
    cmax=0
    for b in linelst:
        try:
            if int(b[-3:-1])>cmax:
                cmax=int(b[-3:-1])
        except:
            continue

f=open("Day2Input.txt",'r')
sm=0
psm=0
for (i,line) in enumerate(f):
    linelstb=line.split("blue")
    linelstr=line.split("red")
    linelstg=line.split("green")
    power=GetMax(linelstb)*GetMax(linelstg)*GetMax(linelstr)
    psm+=power

    if CheckCol(linelstb,14):
        continue

    if CheckCol(linelstg,13):
        continue

    if CheckCol(linelstr,12):
        continue
    
    sm+=i+1
print(sm)

