f=open("Day4Input.txt", 'r')
som=0
for line in f:
    score=1
    linelst=line.split(":")
    linelst=linelst[1].split("|")
    winningnumbers=[]
    for i in range((len(linelst[0])-1)//3):
        winningnumbers.append(int(linelst[0][1+i*3]+linelst[0][2+i*3]))
    for i in range((len(linelst[1])-1)//3):
        number=int(linelst[1][1+i*3]+linelst[1][2+i*3])
        if number in winningnumbers:
            score*=2
    if score>1:
        som+=score//2
print(som)


