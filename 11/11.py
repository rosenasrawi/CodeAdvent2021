# Open data file
def getInput():
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/11/input11.txt", "r") as octopiFile:
        octopi = octopiFile.readlines()
        octopi = [i.rstrip("\n") for i in octopi]
        for i in range(len(octopi)): octopi[i] = list(map(int,octopi[i]))
    return octopi

# octopi = [[5,4,8,3,1,4,3,2,2,3],[2,7,4,5,8,5,4,7,1,1],[5,2,6,4,5,5,6,1,7,3],[6,1,4,1,3,3,6,1,4,6],[6,3,5,7,3,8,5,4,7,8],[4,1,6,7,5,2,4,6,4,5],[2,1,7,6,8,4,1,7,2,1],[6,8,8,2,8,8,1,1,3,4],[4,8,4,6,8,4,8,5,5,4],[5,2,8,3,7,5,1,5,2,6]]

# Find adjacent points in matrix (incl diagonal)
def adjacent(matrix, x, y):
    if x == 0:
        if y == 0: adjIndex = [[x,y+1], [x+1,y], [x+1, y+1]]
        elif y == len(matrix[x])-1: adjIndex = [[x,y-1], [x+1,y], [x+1, y-1]]
        else: adjIndex = [[x,y-1], [x,y+1], [x+1,y], [x+1,y-1], [x+1,y+1]]
    elif x == len(matrix)-1:
        if y == 0: adjIndex = [[x,y+1], [x-1, y], [x-1,y+1]]
        elif y == len(matrix[x])-1: adjIndex = [[x,y-1], [x-1,y], [x-1,y-1]]
        else: adjIndex = [[x,y-1],[x,y+1],[x-1,y], [x-1,y-1], [x-1, y+1]]
    else:
        if y == 0: adjIndex = [[x,y+1], [x-1,y], [x+1,y], [x-1,y+1], [x+1, y+1]]
        elif y == len(matrix[x])-1: adjIndex = [[x,y-1], [x-1,y], [x+1,y], [x-1,y-1], [x+1, y-1]]
        else: adjIndex = [[x,y+1], [x,y-1], [x+1,y], [x-1,y], [x+1,y-1], [x+1,y+1], [x-1,y-1], [x-1,y+1]]

    return adjIndex

# Simulate flashing octopi
def flashingOctopi(octopi):
    flashed = [] # flashed = empty
    queue = []

    for x in range(len(octopi)):
        for y in range(len(octopi[0])):

            if octopi[x][y] >= 9 and [x,y] not in flashed:
                queue.append([x,y])
            octopi[x][y] += 1

            while queue != []:
                next = queue.pop()
                if next not in flashed:
                    flashed.append(next)
                adjIndex = adjacent(octopi, next[0], next[1])

                for i in adjIndex:
                    if octopi[i[0]][i[1]] >= 9 and i not in flashed:
                        flashed.append(i)
                        queue.append(i)
                    else: octopi[i[0]][i[1]] += 1

    for i in flashed: octopi[i[0]][i[1]] = 0
    return len(flashed)

# Part 1 - count total amount of flashes after 100 steps
octopi = getInput(); totalFlashed = 0

for i in range(100):
    totalFlashed += flashingOctopi(octopi)
    
print(totalFlashed)

# Part 2 - find first time all flash simultaneously
octopi = getInput(); simultaneous = False; 
numOctipi = len(octopi)*len(octopi[0]); steps = 0

while not simultaneous:
    flashed = flashingOctopi(octopi); steps+=1
    if flashed == numOctipi:
        simultaneous = True 

print(steps)