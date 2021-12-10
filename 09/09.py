# Open & read data
from os import X_OK


with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/09/input09.txt", "r") as heightmapFile:
    heightMap = heightmapFile.readlines()
    heightMap = [i.rstrip("\n") for i in heightMap]

# print(heightMap)
# heightMap = ['2199943210', '3987894921','9856789892','8767896789','9899965678']

heightMap = [list(map(int,heightMap[i])) for i in range(len(heightMap))]
# print(heightMap)

def adjacent(i,z):

    if i == 0:
        if z == 0: adjIndex = [[i,z+1], [i+1,z]]
        elif z == len(heightMap[i])-1: adjIndex = [[i,z-1], [i+1,z]]
        else: adjIndex = [[i,z-1], [i,z+1], [i+1,z]]
    elif i == len(heightMap)-1:
        if z == 0: adjIndex = [[i,z+1], [i-1, z]]
        elif z == len(heightMap[i])-1: adjIndex = [[i,z-1], [i-1,z]]
        else: adjIndex = [[i,z-1],[i,z+1],[i-1,z]]
    else:
        if z == 0: adjIndex = [[i,z+1],[i-1,z],[i+1,z]]
        elif z == len(heightMap[i])-1: adjIndex = [[i,z-1], [i-1,z],[i+1,z]]
        else: adjIndex = [[i,z+1],[i,z-1],[i-1,z],[i+1,z]]

    return adjIndex

# Part 1: find the lowest points
lowPoint = []; lowIndex = []

for i in range(len(heightMap)):
    for z in range(len(heightMap[i])):

        item = heightMap[i][z]
        adjIndex = adjacent(i,z)
        adj = [heightMap[i[0]][i[1]] for i in adjIndex]
        if sum([item<i for i in adj]) == len(adj):
            lowPoint += [item]
            lowIndex.append([i,z])

lowPoint = list(map(int,lowPoint))
lowPointPlus = [i+1 for i in lowPoint]
print(sum(lowPointPlus))

# Part 2: use lowest points to find largest basin

def searchBasin(first):
    visited = [first]
    queue = [first]

    while queue != []:
        s = queue.pop()
        adjIndex = adjacent(s[0],s[1])

        p = heightMap[s[0]][s[1]]

        for a in adjIndex:
            nextP = heightMap[a[0]][a[1]]

            if a not in visited and nextP >= p and nextP < 9:
                queue.append(a)
                visited.append(a)
    return visited

lenVisited = []
for first in lowIndex:
    lenVisited += [len(searchBasin(first))]

print(sorted(lenVisited))

maxLenVisited = sorted(lenVisited, reverse = True)[:3]
prod = 1
for i in maxLenVisited:
    prod = prod*i

print(prod)