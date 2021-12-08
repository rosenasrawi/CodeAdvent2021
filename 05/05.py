# Open & read data

with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/05/input05.txt", "r") as ventsFile:
    vents = ventsFile.readlines()

y = []

for ven in range(len(vents)):
    x = vents[ven].split(); x.remove('->')
    x = list(map(int, x[0].split(','))) + list(map(int, x[1].split(',')))
    y.append(x)

vents = y.copy()
maxVents = max(sum(vents,[]))+1

def diagramOfDirections(diag):

    diagram = [[0 for col in range(maxVents)] for row in range(maxVents)]
    numTwice = 0

    for coor in range(len(vents)):

        thisCoor = vents[coor]

        if thisCoor[0] == thisCoor[2]:

            xRange = thisCoor[0]

            if thisCoor[1] > thisCoor[3]:
                yRange = list(range(thisCoor[1], thisCoor[3]-1, -1))
            else: yRange = list(range(thisCoor[1],thisCoor[3]+1))
            
            for i in range(len(yRange)):
                diagram[yRange[i]][xRange] +=1
                if diagram[yRange[i]][xRange] == 2:
                    numTwice +=1 
        
        elif thisCoor[1] == thisCoor[3]:

            if thisCoor[0] > thisCoor[2]:
                xRange = list(range(thisCoor[0], thisCoor[2]-1, -1))
            else: xRange = list(range(thisCoor[0],thisCoor[2]+1))        
            
            yRange = thisCoor[1]
            
            for i in range(len(xRange)):
                diagram[yRange][xRange[i]] +=1
                if diagram[yRange][xRange[i]] == 2:
                    numTwice +=1

        elif abs(thisCoor[0]-thisCoor[2]) == abs(thisCoor[1]-thisCoor[3]) and diag == True:
        
            if thisCoor[0] > thisCoor[2]:
                xRange = list(range(thisCoor[0], thisCoor[2]-1, -1))
            else: xRange = list(range(thisCoor[0],thisCoor[2]+1)) 

            if thisCoor[1] > thisCoor[3]:
                yRange = list(range(thisCoor[1], thisCoor[3]-1, -1))
            else: yRange = list(range(thisCoor[1],thisCoor[3]+1)) 

            for i in range(len(xRange)):
                diagram[yRange[i]][xRange[i]] +=1
                if diagram[yRange[i]][xRange[i]] == 2:
                    numTwice +=1

    return numTwice

# Part 1 - Horizontal & vertical lines
print(diagramOfDirections(diag = False))

# Part 2 - Horizontal, vertical, & diagonal lines
print(diagramOfDirections(diag = True))

