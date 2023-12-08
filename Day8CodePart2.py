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
nodedict.update({"XXX":("XXX","XXX")}) #add stable point

#currentnode="AAA"
currentnodeslist=[node for node in nodedict.keys() if node[-1]=="A"]
#startnodeslist=currentnodeslist
periodlist=[0]*len(currentnodeslist)
steps=0
#secondBREAKfast=False
#iteration=0

while True:
    #iteration+=1
    for char in directions:
        currentnodeslist=[nodedict[currentnode][0 if char=="L" else 1] for currentnode in currentnodeslist]
        steps+=1
        for i in range(currentnodeslist):
            if currentnodeslist[i][-1]=="Z":
                periodlist[i]=steps
                currentnodeslist[i]="XXX"
    
    if currentnodeslist==["XXX"]*len(currentnodeslist):
        break
