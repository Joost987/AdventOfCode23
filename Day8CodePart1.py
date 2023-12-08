f=open("Day8Input.txt", 'r')
directions=f.readline()[:-1]
f.readline()


nodedict={}
for line in f:
    nodes=line.split(" ") #extract the nodes from the line
    nodestart=nodes[0]
    nodesleft=nodes[2][1:-1]
    nodesright=nodes[3][:-2]
    nodedict.update({nodestart:(nodesleft,nodesright)})

currentnode="AAA"
steps=0

while True:
    for char in directions:
        currentnode=nodedict[currentnode][0 if char=="L" else 1]
        steps+=1
        if currentnode=="ZZZ":
            print(steps)
            break
    if currentnode=="ZZZ":
        break