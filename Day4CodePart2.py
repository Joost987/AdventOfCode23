f=open("Day4Input.txt", 'r')
lines=f.readlines()

numcards=[1]*len(lines)
for (j,line) in enumerate(lines):
    score=0
    linelst=line.split(":")
    linelst=linelst[1].split("|")
    winningnumbers=[]
    for i in range((len(linelst[0])-1)//3):
        winningnumbers.append(int(linelst[0][1+i*3]+linelst[0][2+i*3]))
    for i in range((len(linelst[1])-1)//3):
        number=int(linelst[1][1+i*3]+linelst[1][2+i*3])
        if number in winningnumbers:
            score+=1
    for i in range(j+1,j+1+score):
        numcards[i]+=numcards[j]
print(sum(numcards))


