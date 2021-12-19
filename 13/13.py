# Open data file
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/13/input13.txt", "r") as instrFile:
    coorInstr = instrFile.readlines()
    coorInstr = [i.rstrip("\n") for i in coorInstr]
    
    i = 0; fold = False
    while not fold:
        if 'fold' in coorInstr[i]: fold = True
        i+=1

    coordinates = coorInstr[:i-2]; instructions = coorInstr[i-1:]

    for coor in range(len(coordinates)): 
        coordinates[coor] = list(map(int,coordinates[coor].split(',')))

    for i in range(len(instructions)):
        inst = instructions[i]; inst = inst.split(); inst = inst[-1].split('='); inst[1] = int(inst[1])
        instructions[i] = inst

# Example data
# coordinates = [[6,10],[0,14],[9,10],[0,3],[10,4],[4,11],[6,0],[6,12],[4,1],[0,13],[10,12],[3,4],[3,0],[8,4],[1,10],[2,14],[8,10],[9,0]]
# instructions = [['y',7], ['x',5]]

# Function to fill paper with coordinates
def coordinatesFill(coordinates, x = [], y = []):
    for i in coordinates: 
        x += [i[0]]; y += [i[1]]    

    paper = [['.' for col in range(max(x)+1)] for row in range(max(y)+1)]

    for coor in coordinates: 
        i = coor[0]; j = coor[1]; paper[j][i] = '#'
    
    return paper

# Function to fold a paper along x or y, at certain number
def foldPaper(newpaper, type, fold, countOverlap = 0):

    if type == 'y':
        paper1 = newpaper[:fold]; paper2 = newpaper[fold+1:]

        r1 = list(range(len(paper1)))           # 0 to end
        r2 = list(range(len(paper2)-1,-1,-1))   # end to 0

        for r in r1:
            row1 = paper1[r]; row2 = paper2[r2[r]]

            for n in range(len(row1)):
                if row2[n] == '#': row1[n] = '#'
            paper1[r] = row1

        for row in paper1:
            countOverlap += row.count('#')
        
    if type == 'x':
        paper1 = []

        for i in range(len(newpaper)):
            row = newpaper[i]; row1 = row[:fold]; row2 = row[fold+1:]

            r1 = list(range(len(row1)))         # 0 to end
            r2 = list(range(len(row2)-1,-1,-1)) # end to 0

            for i in r1:
                if row2[r2[i]] == '#': row1[i] = row2[r2[i]]
            
            paper1.append(row1); countOverlap += row1.count('#')

    return paper1, countOverlap

# Part 1 - fold paper according to first instruction
paper = coordinatesFill(coordinates)
paper1, countOverlap = foldPaper(newpaper = paper, type = instructions[0][0], fold = instructions[0][1])

print(countOverlap)

# Part 2 - fold paper with complete instructions and print letters
paper1 = coordinatesFill(coordinates)

for inst in instructions:
    paper1, countOverlap = foldPaper(newpaper = paper1, type = inst[0], fold = inst[1])

for i in paper1: print(' '.join(i))
