f=open("Day1Input.txt", 'r')
intlist=['0','1','2','3','4','5','6','7','8','9']
numdict={'one': "1", 'two': "2", 'three': '3', "four": "4", "five": '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
sm=0
for line in f:
    lst=[]
    for (i,char) in enumerate(line):
        if char in intlist:
            lst.append(char)
        if  line[i:i+3] in ['one', 'two', 'six']:
            print(line[i:i+3])
            lst.append(numdict[line[i:i+3]])
        if line[i:i+4] in ['four', 'five', 'nine']:
            lst.append(numdict[line[i:i+4]])
        if line[i:i+5] in ['three', 'seven','eight']:
            lst.append(numdict[line[i:i+5]])
    sm+=int(lst[0]+lst[-1])
print(sm)