
f=open("Day3Input.txt", 'r')
inputlst=['.'*142]

for line in f:
    inputlst.append('.'+line[:-1]+'.')
inputlst.append('.'*142)

gearslst=[]
gearscurseen=[]
gearsdict={}
gearrat=0
gearcount=0
gearslstdone=[]

for i in range(1,len(inputlst)-1):
    num=''
    gear=False
    gearscurseen=[]
    for j in range(0,len(inputlst[1])):

        try: 
            int(inputlst[i][j])
            num+=inputlst[i][j]
            for k in [-1,0,1]:
                for m in [-1,0,1]:
                    if k==m==0:
                        continue
                    if ( inputlst[i+k][j+m]=='*'):
                        
                        if not((i+k,j+m) in gearslst):
                            gearslst.append((i+k,j+m))
                            gearcount+=1
                            gear=True
                            gearscurseen.append((i+k,j+m))
                            
                        elif not((i+k,j+m) in gearscurseen):
                            gearcount+=1
                            gear=True
                            gearslst.append((i+k,j+m))


        except(ValueError):
            if gear:
                for count in range(gearcount):
                    if gearslst[-1-count] in gearsdict.keys() and not (gearslst[-1-count] in gearslstdone):
                        gearrat+=int(num)*gearsdict[gearslst[-1-count]]

                        gearslstdone.append(gearslst[-1-count])
                        print(num,gearsdict[gearslst[-1-count]])
                    else:
                        gearsdict.update({gearslst[-1-count]:int(num)})
                gearcount=0
            num=''
            gear=False
            gearscurseen=[]
            continue
print(gearrat)
