def Hash(string):
    curr=0
    for char in string:
        curr+=ord(char)
        curr=((curr%256)*17)%256
    return curr


f=open("Day15Input.txt")
som=0
line=f.readline()
linesplt=line.split("\n")[0].split(",")
for split in linesplt:
    som+=Hash(split)
print(som)