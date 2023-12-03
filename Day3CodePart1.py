f=open("Day3Input.txt", 'r')
inputlst=['.'*142]
sm=0
symbol=False
for line in f:
    inputlst.append('.'+line[:-1]+'.')
inputlst.append('.'*142)

for i in range(1,len(inputlst)-1):
    if symbol:
        sm+=int(num)
    symbol=False
    num=''
    for j in range(1,len(inputlst[1])-1):
        try: 
            int(inputlst[i][j])
            num+=inputlst[i][j]

            for k in [-1,0,1]:
                for m in [-1,0,1]:
                    if k==m==0:
                        continue
                    if not( inputlst[i+k][j+m] in [".",'0','1', '2','3', '4','5','6','7','8','9']):
                        symbol=True

        except(ValueError):
            if symbol:

                sm+=int(num)
            symbol=False
            num= ''
            continue
print(sm)