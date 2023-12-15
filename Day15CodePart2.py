def Hash(string):
    curr=0
    for char in string:
        curr+=ord(char)
        curr=((curr%256)*17)%256
    return curr


f=open("Day15Input.txt")
som=0
boxes=[[] for i in range(256)]
diczak={}
line=f.readline()
linesplt=line.split("\n")[0].split(",")
for split in linesplt:
    if "-" in split:
        symbssplit=split.split("-")
        box=Hash(symbssplit[0])
        if symbssplit[0] in boxes[box]:
            boxes[box].remove(symbssplit[0])
            del diczak[symbssplit[0]]
    elif "=" in split:
        symbssplit=split.split("=")
        box=Hash(symbssplit[0])
        if symbssplit[0] in boxes[box]:
            diczak.update({symbssplit[0]:int(symbssplit[1])})
        else:
            boxes[box].append(symbssplit[0])
            diczak.update({symbssplit[0]:int(symbssplit[1])})

    
for (j,box) in enumerate(boxes):
    for i in range(len(box)):
        som+=(j+1)*(i+1)*diczak[box[i]]
print(som)